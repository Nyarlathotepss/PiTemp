from django.urls import path
from . import views

urlpatterns = [
    path('my_temperatures/', views.home, name="my_temperatures"),
]
