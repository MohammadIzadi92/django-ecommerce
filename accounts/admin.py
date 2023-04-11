from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ("name", "email", "phone_number", "birthday", "sex")
    fieldsets = (
        (
            None,
            {
                "fields": ("name", "phone_number", "birthday", "sex")
            }),
    ) + UserAdmin.fieldsets
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("name", "phone_number", "birthday", "sex", "password1", "password2"),
            },
        ),
    )
