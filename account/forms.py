from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    """Simple form for user registration.

    This is a Sample form for user registration that extend default
    UserCreationForm

    """

    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, required=True,
                             help_text='Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )
