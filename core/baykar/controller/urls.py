from django.urls import path, include
from baykar.controller.views import loginControl, register, logoutControl

urlpatterns = [
    path('login-control/', loginControl, name="login-control"),
    path('register/', register, name="control_register"),
    path('logout/', logoutControl, name="logout"),

]