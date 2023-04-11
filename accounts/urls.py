from django.urls import path
from .views import UsersListAPIView, UserCreateAPIView

urlpatterns = [
    path("", UsersListAPIView.as_view(), name="users_list"),
    path("new/", UserCreateAPIView.as_view(), name="create_user"),
]
