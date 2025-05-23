# dashboard/views.py
from django.shortcuts import render
from .firebase_data import get_plant_data

def dashboard_view(request):
    return render(request, 'dashboard.html')

def analytics_view(request):
    return render(request, 'analytics.html')

