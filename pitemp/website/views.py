from django.shortcuts import render
from .models import Temperature
from website import data_dashboard


def home(request):
    return render(request, 'website/home.html')


def my_dashboard(request):
    """view to display chart with temperatures"""
    information = data_dashboard.DataDashboard()
    current_user = request.user   # get user id
    my_queryset = Temperature.objects.filter(idUser=current_user).order_by('-date')[:12]    # get last 12 temperatures
    information.get_all_information_for_dashboard(my_queryset)
    info_to_display = {'moyenne': information.average, 'last_update': information.last_update_hour}
    context = {'my_temperatures': information.list_temp, 'my_hours': information.list_hours, 'data': info_to_display,
               'msg': information.message_to_display}
    return render(request, 'website/my_dashboard.html', context)
