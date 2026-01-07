from django.db import models

# Create your models here.
class Faction(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = "Faction"
        verbose_name_plural = "Factions"
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Unit(models.Model):
    ROLE = [
        ('core', 'Core'),
        ('hero', 'Hero'),
        ('lord', 'Lord'),
        ('special', 'Special'),
        ('rare', 'Rare'),
    ]
    name = models.CharField(max_length=100)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE, related_name='units')
    role = models.CharField(max_length=10, choices=ROLE)
    points = models.PositiveIntegerField()
    min_size = models.PositiveIntegerField(default=5)
    max_size = models.PositiveIntegerField(default=20)

    class Meta:
        ordering = ['faction', 'name', 'role']
        verbose_name = "Unit"
        verbose_name_plural = "Units"

    def __str__(self):
        return f"{self.name} ({self.faction.name})"