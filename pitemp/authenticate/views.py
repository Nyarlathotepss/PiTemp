from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .forms import CustomUserCreationForm


def my_account(request):
    return render(request, 'authenticate/my_account.html')


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

