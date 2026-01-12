from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from core.models import Faction

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home/home.html"


class WorldPageView(TemplateView):
    template_name = "home/world.html"


class FactionPageView(TemplateView):
    template_name = "home/factions.html"


class FactionDetailView(TemplateView):
    template_name = "home/faction_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        faction_name = kwargs.get('faction_name')
        context['faction'] = get_object_or_404(Faction, name=faction_name)
        return context
