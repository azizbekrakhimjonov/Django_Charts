from django.shortcuts import render
from django.views.generic import ListView
from .models import UserActivate
import matplotlib.pyplot as plt

class UserListView(ListView):
    model = UserActivate
    template_name = 'home.html'
    context_object_name = 'UserActivate'


def chart_view(request):
    # Sample data for xValues and datasets
    x_values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    datasets = [
        [860, 1140, 1060, 1060, 1070, 1110, 1330, 2210, 7830, 2478],
    ]

    return render(request, 'home.html', {
        'x_values': x_values,
        'datasets': datasets
    })