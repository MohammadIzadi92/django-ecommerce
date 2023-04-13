from rest_framework import serializers, exceptions
from rest_framework.serializers import ModelSerializer
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError as DjangoValidationError
from django.contrib.auth import authenticate
from allauth.account.adapter import get_adapter
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import exceptions as url_exceptions
from .models import CustomUser


class LoginSerializer(serializers.Serializer):
    """
    This class is custom LoginSerializer for dj_rest_auth login
    """

    # fields
    phone_number = serializers.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                regex=r"(09\d{9})",
                message="Phone number must be entered in the format '09000000000'. Up to 11 digits allowed.",
            )
        ]
    )
    password = serializers.CharField(write_only=True)

    def authenticate(self, **kwargs):
        """
        Authenticated method. Used by _validate_phone_number method.
        """
        return authenticate(self.context['request'], **kwargs)

    def _validate_phone_number(self, phone_number, password):
        """
        This method validates phone number.
        """
        if phone_number and password:
            user = self.authenticate(
                phone_number=phone_number, password=password)
        else:
            msg = _('Must include "phone_number" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def get_auth_user(self, phone_number, password):
        """
        This method returns the authenticated user instance if credentials are correct,
        else 'None' will be returned.
        """
        if 'allauth' in settings.INSTALLED_APPS:
            try:
                return self._validate_phone_number(phone_number, password)
            except url_exceptions.NoReverseMatch:
                msg = _('Unable to log in with provided credentials.')
                raise exceptions.ValidationError(msg)
        return None

    @staticmethod
    def validate_auth_user_status(user):
        """
        If user is not active rasie an exceptions
        """
        if not user.is_active:
            msg = _('User account is disabled.')
            raise exceptions.ValidationError(msg)

    def validate(self, attrs):
        """
        Validate and return user
        """
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')
        user = self.get_auth_user(phone_number, password)
        if not user:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)
        self.validate_auth_user_status(user)
        attrs['user'] = user
        return attrs


class RegisterSerializer(ModelSerializer):
    """
    This class is custom RegisterSerializer for dj_rest_auth registration
    """
    
    # needed fields
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        # model fields
        fields = ("first_name", "last_name", "phone_number",
                  "birthday", "sex", "password1", "password2")

    def validate_password1(self, password):
        """
        Validate password for user registration
        """
        return get_adapter().clean_password(password)

    def validate(self, data):
        """
        This method checks equality of password1 and password2
        """
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                _("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        """
        This method cleans and returns all registration fields.
        """
        return {
            'phone_number': self.validated_data.get('phone_number', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'birthday': self.validated_data.get('birthday', ''),
            'sex': self.validated_data.get('sex', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get("email", '')
        }

    def save(self, request):
        """
        This function takes the fields related to the user and saves them
        """
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self, commit=False)
        if "password1" in self.cleaned_data:
            try:
                adapter.clean_password(
                    self.cleaned_data['password1'], user=user)
            except DjangoValidationError as exc:
                raise serializers.ValidationError(
                    detail=serializers.as_serializer_error(exc)
                )
        user.username = self.cleaned_data.get("username", "")
        user.phone_number = self.cleaned_data.get("phone_number")
        user.first_name = self.validated_data.get("first_name")
        user.last_name = self.validated_data.get("last_name")
        user.birthday = self.cleaned_data.get("birthday")
        user.sex = self.cleaned_data.get("sex")
        user.save()
        return user


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    class Meta:
        model = CustomUser
        fields = ('pk', "first_name", "last_name",
                  "phone_number", "birthday", "sex")
