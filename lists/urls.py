from django.urls import path
from .views import ArmyListListView, ArmyListDetailView, ArmyListCreateView

urlpatterns = [
    path('', ArmyListListView.as_view(), name='armylist_list'),
    path('create/', ArmyListCreateView.as_view(), name='armylist_create'),
    path('<int:pk>/', ArmyListDetailView.as_view(), name='armylist_detail'),
]
