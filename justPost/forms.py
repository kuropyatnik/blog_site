from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    about_me = forms.CharField(max_length=250, help_text='Optional. Tell about yourself in 250 symbols.', required=False)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email', 'about_me', 'password1', 'password2', )