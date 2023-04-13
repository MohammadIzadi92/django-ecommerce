from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from .custom_user_manager import CustomUserManager

# Create your models here.


class CustomUser(AbstractUser):
    """
    Personalize django default user
    """
    SEX_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),
    )
    username = models.CharField(_('username'), max_length=50, blank=True)
    phone_number = models.CharField(
        _('phone number'),
        unique=True,
        max_length=11,
        validators=[
            RegexValidator(
                regex=r"(09\d{9})",
                message="Phone number must be entered in the format '09000000000'. Up to 11 digits allowed.",
            )
        ]
    )
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    birthday = models.DateField(_('birthday'))
    sex = models.CharField(
        _('sex'),
        max_length=6,
        choices=SEX_CHOICES,
        validators=[
            RegexValidator(
                regex=r"(male)|(female)",
                message="Sex must be one of these two options 'male or female'.",
            )
        ]
    )

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["first_name", "last_name", "birthday", "sex"]
    # change user manager
    object = CustomUserManager()
