from rest_framework.serializers import ModelSerializer
from .models import CustomUser


class UsersSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("name", "phone_number", "password", "birthday", "sex")
