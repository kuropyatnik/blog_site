from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    about_me = forms.CharField(max_length=250, help_text='Расскажите о себе (если хотите) в 250 символах', required=False)
    email = forms.EmailField(max_length=254, help_text='Обязательное поле. Введите валидный адрес электронной почты')
    class Meta:
        model = User
        fields = ('username', 'email', 'about_me', 'password1', 'password2', )