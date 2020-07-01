from django.shortcuts import render
import json


def home(request):
    return render(request, 'website/home.html')


def my_dashboard(request):
    my_temperatures = [
                        {'x': '18:00', 'y': '21.05'},
                        {'x': '19:00', 'y': '23.01'},
                        {'x': '20:00', 'y': '20.55'},
                        {'x': '21:00', 'y': '30.01'},
    ]

    context = {'my_temperatures': json.dumps(my_temperatures)}
    print(context)
    return render(request, 'website/my_dashboard.html', context)
