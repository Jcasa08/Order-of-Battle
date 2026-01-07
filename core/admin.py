from django.contrib import admin
from .models import Faction, Unit
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Unit)
class UnitAdmin(SummernoteModelAdmin):
    list_display = ('name', 'faction', 'role', 'points', 'min_size', 'max_size')
    list_filter = ('faction', 'role')
    search_fields = ('name',)


# Register your models here.
admin.site.register(Faction)