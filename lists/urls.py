from django.urls import path
from .views import ArmyListListView, ArmyListDetailView

urlpatterns = [
    path('', ArmyListListView.as_view(), name='armylist_list'),
    path('<int:pk>/', ArmyListDetailView.as_view(), name='armylist_detail'),
]
