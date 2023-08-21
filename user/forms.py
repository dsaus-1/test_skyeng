from django.contrib.auth.forms import UserCreationForm
from user.models import User


class CustomRegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', )
