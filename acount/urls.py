from django.contrib import admin
from django.urls import path
from acount.views import UserRegistrationView,UserLoginView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    
]
