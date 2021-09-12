from django import forms
from .models import Profile
from django.contrib.auth import forms as forms_user

class LoginForm(forms.Form):
    user = forms.CharField(label="Usuário", widget=forms.TextInput(attrs={'placeholder': "Usuário"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Senha"}))

class ProfileChangeForm(forms_user.UserChangeForm):
    class Meta(forms_user.UserChangeForm.Meta):
        model = Profile


class ProfileCreationForm(forms_user.UserCreationForm):
    class Meta(forms_user.UserCreationForm.Meta):
        model = Profile