
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authenticate.forms import CustomUserCreationForm, CustomUserChangeForm
from website.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'adress', 'city', 'postal_code']


admin.site.register(CustomUser, CustomUserAdmin)
