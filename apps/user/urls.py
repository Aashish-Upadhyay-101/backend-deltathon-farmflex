from django.urls import path 
from . import views


urlpatterns = [
    path("signup/", views.UserRegistrationView.as_view(), name="signup-user"),
    path("login/", views.UserLoginView.as_view(), name="login_user"),
    path("user/", views.UserProfileView.as_view(), name="user"),
    path("activate-link/<str:username>/", views.ActivateAccount.as_view(), name="activate-link"),
    path("activate-account/<str:uid>/<str:token>/", views.VerifyAndActivateAccount.as_view(), name="activate-account"),
]
