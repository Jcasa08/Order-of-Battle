from django.urls import path
from .views import (
    ArmyListListView,
    ArmyListDetailView,
    ArmyListCreateView,
    ArmyListUpdateView,
    ArmyListDeleteView,
    AddUnitToArmyListView,
    RemoveUnitFromArmyListView,
    UpdateListUnitView,
    DuplicateArmyListView,
)

urlpatterns = [
    path('', ArmyListListView.as_view(), name='armylist_list'),
    path('create/', ArmyListCreateView.as_view(), name='armylist_create'),
    path('<int:pk>/', ArmyListDetailView.as_view(), name='armylist_detail'),
    path('<int:pk>/edit/', ArmyListUpdateView.as_view(), name='armylist_update'),
    path('<int:pk>/delete/', ArmyListDeleteView.as_view(), name='armylist_delete'),
    path('<int:pk>/add-unit/', AddUnitToArmyListView.as_view(),
         name='add_unit_to_list'),
    path('<int:pk>/duplicate/', DuplicateArmyListView.as_view(),
         name='duplicate_armylist'),
    path('unit/<int:pk>/remove/', RemoveUnitFromArmyListView.as_view(),
         name='remove_unit_from_list'),
    path('unit/<int:pk>/update/', UpdateListUnitView.as_view(),
         name='update_list_unit'),
]
