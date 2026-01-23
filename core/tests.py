# core/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from core.models import Faction, Unit


class UnitDetailsAPITests(TestCase):
    def setUp(self):
        faction = Faction.objects.create(name="Orc Tribes")
        self.unit = Unit.objects.create(
            name="Warband",
            faction=faction,
            role="core",
            points=120,
            min_size=5,
            max_size=20,
        )
        self.client = Client()

    def test_unit_details_returns_json(self):
        resp = self.client.get(reverse("unit_details", args=[self.unit.id]))
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data["min_size"], self.unit.min_size)
        self.assertEqual(data["max_size"], self.unit.max_size)
        self.assertEqual(data["points"], self.unit.points)

    def test_unit_details_missing_returns_404(self):
        resp = self.client.get(reverse("unit_details", args=[9999]))
        self.assertEqual(resp.status_code, 404)
