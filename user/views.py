from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from user.models import User
from user.forms import CustomRegisterUserForm
from django.contrib.auth.forms import AuthenticationForm


class CustomRegisterView(CreateView):
    model = User
    form_class = CustomRegisterUserForm
    success_url = '/'

class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    form_class = AuthenticationForm
