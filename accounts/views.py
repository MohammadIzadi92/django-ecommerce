from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import CustomUser
from .serializers import UsersSerializer, CreateUserSerializer

# Create your views here.


class UsersListAPIView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = CreateUserSerializer
