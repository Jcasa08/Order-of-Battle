from . import views
from django.urls import path, include

urlpatterns = [
    path('api/unit/<int:unit_id>/', views.unit_details, name='unit_details'),
    path('accounts/', include('allauth.urls')),
]
