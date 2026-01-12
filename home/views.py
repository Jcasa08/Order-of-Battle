from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = "home/home.html"

class WorldPageView(TemplateView):
    template_name = "home/world.html"