from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    about_me = forms.CharField(max_length=250, help_text='Расскажите о себе (если хотите) в 250 символах', required=False,)
    email = forms.EmailField(max_length=254, help_text='Обязательное поле. Введите валидный адрес электронной почты',)

    class Meta:
        model = User
        fields = ('username', 'email', 'about_me', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите электронную почту'
        self.fields['about_me'].widget.attrs['placeholder'] = 'Расскажите о себе'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password', )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'