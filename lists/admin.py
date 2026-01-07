from django.contrib import admin
from .models import ArmyList, ListUnit

# Register your models here.
@admin.register(ArmyList)
class ArmyListAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'faction', 'point_limit',
                    'total_points', 'created_on', 'updated_on')
    list_filter = ('faction', 'owner')
    search_fields = ('name', 'owner__username')

@admin.register(ListUnit)
class ListUnitAdmin(admin.ModelAdmin):
    list_display = ('army_list', 'unit', 'quantity', 'subtotal_points')
    list_filter = ('army_list__faction', 'unit__role')
    search_fields = ('army_list__name', 'unit__name')
    readonly_fields = ('subtotal_points',)