from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import TextInput
from django import forms
from .models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField( #메타 클래스가 없음
        widget = forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: skyblue;'}),
        label='유저이름'
    )


class UserSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

        fields = [
            'username'
        ]

        widgets = {
          'username': TextInput(attrs={
            'class': "form-control",
            'style': 'background-color: skyblue;',
            'placeholder': 'ID'
          }),
        }

        labels = {
          'username': 'ID',
        }