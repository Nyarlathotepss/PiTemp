from django.urls import path
from . import views

urlpatterns = [
    path('my_dashboard/', views.my_dashboard, name="my_dashboard"),
]
