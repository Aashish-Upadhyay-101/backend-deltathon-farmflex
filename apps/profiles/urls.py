from django.urls import path 
from . import views 

# create url patterns here
urlpatterns = [
    path("me/", views.GetMyProfileAPIView.as_view(), name="me"),
    path("<str:username>/", views.GetUpdateProfileView.as_view(), name="update_profile"),
]

