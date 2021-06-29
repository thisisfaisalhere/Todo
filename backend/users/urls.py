from django.urls import path
from .views import ( RegisterAPIView, VerifyEmailView,
    LoginAPIView, LogoutAPIView, RequestPasswordResetEmail, SetNewPasswordAPIView,
    ChangePasswordView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    # user register view
    path('register/', RegisterAPIView.as_view(), name="register"),
    path('email-verify/', VerifyEmailView.as_view(), name="email-verify"),

    # login and logout view
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),

    # token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # forgot password
    path('request_reset_email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('reset_password/<uidb64>/<token>/', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete'),
    
    # password reset
    path('password_change/', ChangePasswordView.as_view(),
         name='password-reset-complete'),
]