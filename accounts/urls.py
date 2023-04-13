from django.urls import path
from dj_rest_auth.app_settings import api_settings
from dj_rest_auth.views import LoginView, LogoutView, PasswordChangeView, UserDetailsView
from dj_rest_auth.registration.views import RegisterView

app_name = "accounts"

urlpatterns = [
    # URLs that do need access token
    path('login/', LoginView.as_view(), name='rest_login'),
    path('user/', UserDetailsView.as_view(), name='rest_user_details'),
    # URLs that do not need access token
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('password/change/', PasswordChangeView.as_view(),
         name='rest_password_change'),
    # registration
    path('registration/', RegisterView.as_view(), name='rest_register'),
]

# access and refresh token
if api_settings.USE_JWT:
    from rest_framework_simplejwt.views import TokenVerifyView

    from dj_rest_auth.jwt_auth import get_refresh_view

    urlpatterns += [
        path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
        path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    ]
