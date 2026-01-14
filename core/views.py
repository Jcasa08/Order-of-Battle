from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Unit

# Create your views here.


@require_http_methods(["GET"])
def unit_details(request, unit_id):
    """API endpoint to get unit details (min_size, max_size, points)"""
    try:
        unit = Unit.objects.get(id=unit_id)
        return JsonResponse({
            'min_size': unit.min_size,
            'max_size': unit.max_size,
            'points': unit.points,
        })
    except Unit.DoesNotExist:
        return JsonResponse({'error': 'Unit not found'}, status=404)
