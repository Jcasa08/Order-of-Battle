# home/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from core.models import Faction

class HomeViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.faction = Faction.objects.create(name="Duchies of Men")

    def test_home_page_renders(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home/home.html")

    def test_world_page_renders(self):
        resp = self.client.get(reverse("world"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home/world.html")

    def test_factions_page_renders(self):
        resp = self.client.get(reverse("factions"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home/factions.html")

    def test_faction_detail_existing(self):
        resp = self.client.get(reverse("faction_detail", args=[self.faction.name]))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context["faction"].name, self.faction.name)

    def test_faction_detail_missing_returns_404(self):
        resp = self.client.get(reverse("faction_detail", args=["Nonexistent"]))
        self.assertEqual(resp.status_code, 404)
