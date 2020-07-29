from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .forms import CustomUserCreationForm
from rest_framework.authtoken.models import Token


def my_account(request):
    id = str(request.user.id)
    token = Token.objects.filter(user_id=id)
    token = token[0]
    context = {
                'my_token': token,
                }
    return render(request, 'authenticate/my_account.html', context)


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

