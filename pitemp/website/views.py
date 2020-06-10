from django.shortcuts import render


def home(request):
    return render(request, 'website/home.html')


def my_temperatures(request):
    return render(request, 'website/temperatures.html')
