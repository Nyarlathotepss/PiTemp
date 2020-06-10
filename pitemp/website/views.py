from django.shortcuts import render


def home(request):
    return render(request, 'website/home.html')


def my_dashboard(request):
    return render(request, 'website/my_dashboard.html')
