from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.db.models import Sum
from django.views import View
from .models import ArmyList, ListUnit
from core.models import Unit


class ArmyListListView(ListView):
    """Display all army lists"""
    model = ArmyList
    template_name = 'lists/armylist_list.html'
    context_object_name = 'army_lists'
    paginate_by = 10


class ArmyListDetailView(DetailView):
    """Show a single army list with all its units"""
    model = ArmyList
    template_name = 'lists/armylist_detail.html'
    context_object_name = 'army_list'


class ArmyListCreateView(CreateView):
    """Create a new army list"""
    model = ArmyList
    template_name = 'lists/armylist_form.html'
    fields = ['name', 'owner', 'faction', 'point_limit']

    def form_valid(self, form):
        messages.success(self.request, f'Army list "{form.instance.name}" created successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('armylist_detail', kwargs={'pk': self.object.pk})


class ArmyListUpdateView(UpdateView):
    """Edit an existing army list"""
    model = ArmyList
    template_name = 'lists/armylist_form.html'
    fields = ['name', 'owner', 'faction', 'point_limit']

    def form_valid(self, form):
        messages.success(self.request, f'Army list "{form.instance.name}" updated successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('armylist_detail', kwargs={'pk': self.object.pk})


class ArmyListDeleteView(DeleteView):
    """Delete an army list"""
    model = ArmyList
    template_name = 'lists/armylist_confirm_delete.html'
    success_url = reverse_lazy('armylist_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, f'Army list "{self.get_object().name}" deleted successfully!')
        return super().delete(request, *args, **kwargs)


class AddUnitToArmyListView(View):
    """Add a unit to an army list"""

    def post(self, request, pk):
        army_list = get_object_or_404(ArmyList, pk=pk)
        unit_id = request.POST.get('unit_id')
        quantity = int(request.POST.get('quantity', 5))

        unit = get_object_or_404(Unit, pk=unit_id)

        # Check if unit belongs to the same faction
        if unit.faction != army_list.faction:
            messages.error(request, f'Unit "{unit.name}" does not belong to faction "{army_list.faction.name}"!')
            return redirect('armylist_detail', pk=pk)

        # Create or update the ListUnit
        list_unit, created = ListUnit.objects.get_or_create(
            army_list=army_list,
            unit=unit,
            defaults={'quantity': quantity}
        )

        if not created:
            list_unit.quantity += quantity
            list_unit.save()

        # Calculate subtotal
        list_unit.subtotal_points = list_unit.quantity * unit.points
        list_unit.save()

        # Update army list total
        army_list.total_points = army_list.list_units.aggregate(
            total=Sum('subtotal_points'))['total'] or 0
        army_list.save()

        messages.success(request, f'Added {quantity} x {unit.name} to {army_list.name}')
        return redirect('armylist_detail', pk=pk)


class RemoveUnitFromArmyListView(View):
    """Remove a unit from an army list"""

    def post(self, request, pk):
        list_unit = get_object_or_404(ListUnit, pk=pk)
        army_list = list_unit.army_list
        unit_name = list_unit.unit.name

        list_unit.delete()

        # Update army list total
        army_list.total_points = army_list.list_units.aggregate(
            total=Sum('subtotal_points'))['total'] or 0
        army_list.save()

        messages.success(request, f'Removed {unit_name} from {army_list.name}')
        return redirect('armylist_detail', pk=army_list.pk)


class UpdateListUnitView(View):
    """Update quantity of a unit in a list"""

    def post(self, request, pk):
        list_unit = get_object_or_404(ListUnit, pk=pk)
        new_quantity = int(request.POST.get('quantity', list_unit.quantity))

        if new_quantity <= 0:
            messages.error(request, 'Quantity must be greater than 0!')
            return redirect('armylist_detail', pk=list_unit.army_list.pk)

        list_unit.quantity = new_quantity
        list_unit.subtotal_points = list_unit.quantity * list_unit.unit.points
        list_unit.save()

        # Update army list total
        army_list = list_unit.army_list
        army_list.total_points = army_list.list_units.aggregate(
            total=Sum('subtotal_points'))['total'] or 0
        army_list.save()

        messages.success(request, f'Updated {list_unit.unit.name} quantity to {new_quantity}')
        return redirect('armylist_detail', pk=army_list.pk)


class DuplicateArmyListView(View):
    """Create a copy of an existing army list"""

    def post(self, request, pk):
        original_list = get_object_or_404(ArmyList, pk=pk)

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
                quantity=list_unit.quantity,
                subtotal_points=list_unit.subtotal_points
            )

        messages.success(request, f'Created a copy of "{original_list.name}"!')
        return redirect('armylist_detail', pk=new_list.pk)