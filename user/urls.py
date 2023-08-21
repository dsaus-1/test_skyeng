from django.contrib.auth.views import LogoutView
from django.urls import path
from user.apps import UserConfig
from django.contrib.auth.views import LogoutView
from user.views import CustomLoginView,CustomRegisterView 


app_name = UserConfig.name


urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]