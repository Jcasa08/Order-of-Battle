from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Sum
from django.views import View
from .models import ArmyList, ListUnit
from core.models import Unit


class ArmyListListView(LoginRequiredMixin, ListView):
    """Display user's army lists"""
    model = ArmyList
    template_name = 'lists/armylist_list.html'
    context_object_name = 'army_lists'
    paginate_by = 10
    login_url = 'account_login'
    redirect_field_name = 'next'

    def get_queryset(self):
        """Filter to show only the current user's army lists"""
        print(f"DEBUG: Fetching army lists for user: {self.request.user}")
        return ArmyList.objects.filter(owner=self.request.user).order_by('-updated_on')


class ArmyListDetailView(LoginRequiredMixin, DetailView):
    """Show a single army list with all its units"""
    model = ArmyList
    template_name = 'lists/armylist_detail.html'
    context_object_name = 'army_list'
    login_url = 'account_login'
    redirect_field_name = 'next'

    def get_object(self, queryset=None):
        """Ensure user can only access their own lists"""
        obj = super().get_object(queryset)
        if obj.owner != self.request.user:
            raise PermissionDenied(
                "You do not have permission to view this army list.")
        return obj


class ArmyListCreateView(LoginRequiredMixin, CreateView):
    """Create a new army list"""
    model = ArmyList
    template_name = 'lists/armylist_form.html'
    fields = ['name', 'faction', 'point_limit']
    login_url = 'account_login'
    redirect_field_name = 'next'

    def form_valid(self, form):
        """Set the owner to the current user"""
        form.instance.owner = self.request.user
        messages.success(
            self.request, f'Army list "{form.instance.name}" created successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('armylist_detail', kwargs={'pk': self.object.pk})


class ArmyListUpdateView(LoginRequiredMixin, UpdateView):
    """Edit an existing army list"""
    model = ArmyList
    template_name = 'lists/armylist_form.html'
    fields = ['name', 'faction', 'point_limit']
    login_url = 'account_login'
    redirect_field_name = 'next'

    def get_object(self, queryset=None):
        """Ensure user can only edit their own lists"""
        obj = super().get_object(queryset)
        if obj.owner != self.request.user:
            raise PermissionDenied(
                "You do not have permission to edit this army list.")
        return obj

    def form_valid(self, form):
        messages.success(
            self.request, f'Army list "{form.instance.name}" updated successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('armylist_detail', kwargs={'pk': self.object.pk})


class ArmyListDeleteView(LoginRequiredMixin, DeleteView):
    """Delete an army list"""
    model = ArmyList
    template_name = 'lists/armylist_confirm_delete.html'
    success_url = reverse_lazy('armylist_list')
    login_url = 'account_login'
    redirect_field_name = 'next'

    def get_object(self, queryset=None):
        """Ensure user can only delete their own lists"""
        obj = super().get_object(queryset)
        if obj.owner != self.request.user:
            raise PermissionDenied(
                "You do not have permission to delete this army list.")
        return obj

    def form_valid(self, form):
        """Add success message when deletion is confirmed"""
        messages.success(
            self.request, f'Army list "{self.object.name}" deleted successfully!')
        return super().form_valid(form)


class AddUnitToArmyListView(LoginRequiredMixin, View):
    """Add a unit to an army list"""
    login_url = 'account_login'
    redirect_field_name = 'next'

    def post(self, request, pk):
        army_list = get_object_or_404(ArmyList, pk=pk)

        # Check if user owns this list
        if army_list.owner != request.user:
            raise PermissionDenied(
                "You do not have permission to modify this army list.")

        unit_id = request.POST.get('unit_id')
        quantity = int(request.POST.get('quantity', 5))

        unit = get_object_or_404(Unit, pk=unit_id)

        # Read and validate unit_size from form (default to unit.min_size)
        try:
            unit_size = int(request.POST.get('unit_size', unit.min_size))
        except (TypeError, ValueError):
            unit_size = unit.min_size

        # Ensure unit_size is valid: between min/max and multiple of min_size
        if (
            unit_size < unit.min_size or
            unit_size > unit.max_size or
            unit_size % unit.min_size != 0
        ):
            messages.error(
                request,
                f'Invalid unit size for {unit.name}. Choose between {unit.min_size} and {unit.max_size} in steps of {unit.min_size}.'
            )
            return redirect('armylist_detail', pk=pk)

        # Check if unit belongs to the same faction
        if unit.faction != army_list.faction:
            messages.error(
                request, f'Unit "{unit.name}" does not belong to faction "{army_list.faction.name}"!')
            return redirect('armylist_detail', pk=pk)

        # Create or update the ListUnit
        list_unit, created = ListUnit.objects.get_or_create(
            army_list=army_list,
            unit=unit,
            defaults={'quantity': quantity, 'unit_size': unit_size}
        )

        if not created:
            # Update unit_size to selected value and increment quantity
            list_unit.unit_size = unit_size
            list_unit.quantity += quantity
            list_unit.save()

        # Scaled points for the selected unit_size
        scaled_unit_points = (unit.points * unit_size) // unit.min_size

        # Calculate subtotal (quantity * scaled points)
        list_unit.subtotal_points = list_unit.quantity * scaled_unit_points
        list_unit.save()

        # Update army list total
        army_list.total_points = army_list.list_units.aggregate(
            total=Sum('subtotal_points'))['total'] or 0
        army_list.save()

        messages.success(
            request, f'Added {quantity} x {unit.name} to {army_list.name}')
        return redirect('armylist_detail', pk=pk)
        return redirect('armylist_detail', pk=pk)


class RemoveUnitFromArmyListView(LoginRequiredMixin, View):
    """Remove a unit from an army list"""
    login_url = 'account_login'
    redirect_field_name = 'next'

    def post(self, request, pk):
        list_unit = get_object_or_404(ListUnit, pk=pk)
        army_list = list_unit.army_list

        # Check if user owns this list
        if army_list.owner != request.user:
            raise PermissionDenied(
                "You do not have permission to modify this army list.")

        unit_name = list_unit.unit.name

        list_unit.delete()

        # Update army list total
        army_list.total_points = army_list.list_units.aggregate(
            total=Sum('subtotal_points'))['total'] or 0
        army_list.save()

        messages.success(request, f'Removed {unit_name} from {army_list.name}')
        return redirect('armylist_detail', pk=army_list.pk)


class UpdateListUnitView(LoginRequiredMixin, View):
    """Update quantity of a unit in a list"""
    login_url = 'account_login'
    redirect_field_name = 'next'

    def post(self, request, pk):
        list_unit = get_object_or_404(ListUnit, pk=pk)
        army_list = list_unit.army_list

        # Check if user owns this list
        if army_list.owner != request.user:
            raise PermissionDenied(
                "You do not have permission to modify this army list.")

        new_quantity = int(request.POST.get('quantity', list_unit.quantity))

        if new_quantity <= 0:
            messages.error(request, 'Quantity must be greater than 0!')
            return redirect('armylist_detail', pk=army_list.pk)

        list_unit.quantity = new_quantity
        # Use scaled points according to unit_size
        scaled_unit_points = (list_unit.unit.points * (
            list_unit.unit_size or list_unit.unit.min_size)) // list_unit.unit.min_size
        list_unit.subtotal_points = list_unit.quantity * scaled_unit_points
        list_unit.save()

        # Update army list total
        army_list.total_points = army_list.list_units.aggregate(
            total=Sum('subtotal_points'))['total'] or 0
        army_list.save()

        messages.success(
            request, f'Updated {list_unit.unit.name} quantity to {new_quantity}')
        return redirect('armylist_detail', pk=army_list.pk)


class DuplicateArmyListView(LoginRequiredMixin, View):
    """Create a copy of an existing army list"""
    login_url = 'account_login'
    redirect_field_name = 'next'

    def post(self, request, pk):
        original_list = get_object_or_404(ArmyList, pk=pk)

        # Check if user owns this list
        if original_list.owner != request.user:
            raise PermissionDenied(
                "You do not have permission to duplicate this army list.")

        # Create a copy of the army list
        new_list = ArmyList.objects.create(
            name=f"Copy of {original_list.name}",
            owner=original_list.owner,
            faction=original_list.faction,
            point_limit=original_list.point_limit,
            total_points=original_list.total_points
        )

        # Copy all list units
        for list_unit in original_list.list_units.all():
            ListUnit.objects.create(
                army_list=new_list,
                unit=list_unit.unit,
                unit_size=list_unit.unit_size or list_unit.unit.min_size,
                quantity=list_unit.quantity,
                subtotal_points=list_unit.subtotal_points
            )

        messages.success(request, f'Created a copy of "{original_list.name}"!')
        return redirect('armylist_detail', pk=new_list.pk)
