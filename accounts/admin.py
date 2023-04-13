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
    list_display = ("phone_number", "first_name", "last_name", "birthday", "sex")
    fieldsets = (
        (
            None,
            {
                "fields": ("phone_number", "birthday", "sex")
            }),
    ) + UserAdmin.fieldsets
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "phone_number", "birthday", "sex", "password1", "password2"),
            },
        ),
    )
