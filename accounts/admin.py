from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    In this class we change some attributes of UserAdmin
    """
    model = CustomUser
    
    # List of fields for disply in admin panel
    list_display = ("phone_number", "first_name",
                    "last_name", "birthday", "sex")
    
    # Add some fields in admin chage form
    fieldsets = (
        (
            None,
            {
                "fields": ("phone_number", "birthday", "sex")
            }),
    ) + UserAdmin.fieldsets
    
    # Add some fields in admin creation form
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "phone_number", "birthday", "sex", "password1", "password2"),
            },
        ),
    )
