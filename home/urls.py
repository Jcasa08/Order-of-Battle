from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("world/", views.WorldPageView.as_view(), name="world"),
    path("factions/", views.FactionPageView.as_view(), name="factions"),
    path("factions/<str:faction_name>/",
         views.FactionDetailView.as_view(), name="faction_detail"),
]
