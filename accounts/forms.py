from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import NewUser


class RegisterForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ["first_name", "last_name", "username", "password1", "password2"]


class LoginForm(AuthenticationForm):
    pass

