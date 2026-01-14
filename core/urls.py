from . import views
from django.urls import path

urlpatterns = [
    path('api/unit/<int:unit_id>/', views.unit_details, name='unit_details'),
]
