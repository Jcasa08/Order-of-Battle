from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("world/", views.WorldPageView.as_view(), name="world"),
]
