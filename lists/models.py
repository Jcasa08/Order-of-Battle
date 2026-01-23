from django.db import models
from django.contrib.auth.models import User
from core.models import Faction, Unit

# Create your models here.


class ArmyList(models.Model):
    name = models.CharField(max_length=200, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='army_lists')
    faction = models.ForeignKey(Faction, on_delete=models.PROTECT,
                                related_name='army_lists')
    point_limit = models.PositiveIntegerField(blank=True, null=True)
    total_points = models.PositiveIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_on']
        verbose_name = "Army List"
        verbose_name_plural = "Army Lists"
        indexes = [models.Index(fields=['owner', 'faction'])]

    def __str__(self):
        return (f"{self.name} - {self.faction.name} "
                f"({self.total_points} pts)"
                f"\n created by {self.owner.username}")


class ListUnit(models.Model):
    army_list = models.ForeignKey(
        ArmyList, on_delete=models.CASCADE, related_name='list_units')
    unit = models.ForeignKey(
        Unit, on_delete=models.PROTECT, related_name='list_units')
    unit_size = models.PositiveIntegerField(
        default=None, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=5)
    subtotal_points = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "List Unit"
        verbose_name_plural = "List Units"
        ordering = ['army_list', 'unit__faction', 'unit__name']

    def __str__(self):
        return f"{self.quantity} x {self.unit.name} in {self.army_list.name}"

    def scaled_points(self):
        """Points per unit, scaled by current unit_size.
        If unit_size is not set, default to unit.min_size.
        """
        size = self.unit_size or self.unit.min_size
        return (self.unit.points * size) // self.unit.min_size
