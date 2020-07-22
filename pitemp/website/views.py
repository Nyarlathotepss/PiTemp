from django.shortcuts import render
from .models import Temperature
import json


def home(request):
    return render(request, 'website/home.html')


def my_dashboard(request):
    """view to display chart with temperatures"""

    info_to_display = {'moyenne': '12', 'last_update': '13h'}
    current_user = request.user   # get user id
    temperatures = Temperature.objects.filter(idUser=current_user).order_by('-date')[:12]    # get last 12 temperatures
    print(temperatures.values())
    my_temperatures = []
    message_to_display = str()
    if temperatures.first():
        for i in temperatures:
            print(i.temperature, i.date)
            date = str(i.date)
            date = date[11:13]+'h'
            print(date)
            my_temperatures.append({'x': date, 'y': i.temperature},)
    else:
        message_to_display = 'Pas d''informations à afficher'

    context = {'my_temperatures': json.dumps(my_temperatures), 'data': info_to_display, 'msg': message_to_display}
    return render(request, 'website/my_dashboard.html', context)
