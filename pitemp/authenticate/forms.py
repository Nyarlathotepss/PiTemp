from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from website.models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'adress', 'city', 'postal_code')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'adress', 'city', 'postal_code')
