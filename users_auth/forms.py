from django import forms
from .models import Profile
from django.contrib.auth import forms as forms_user
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    user = forms.CharField(label="Usuário", widget=forms.TextInput(attrs={'placeholder': "Usuário"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Senha"}))

class ProfileChangeForm(forms_user.UserChangeForm):
    class Meta(forms_user.UserChangeForm.Meta):
        model = Profile


class ProfileCreationForm(forms_user.UserCreationForm):
    class Meta(forms_user.UserCreationForm.Meta):
        model = Profile


class ProfileForm(UserCreationForm):
    code = forms.CharField(label='código', max_length=11)
    first_name = forms.CharField(label="Nome")
    last_name = forms.CharField(label='Sobrenome')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Telefone')
    profile_type = forms.ChoiceField(choices=Profile.PROFILE_TYPE_CHOICES)
    about = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'placeholder': 'Digite algo sobre você'}))

    class Meta:
        model = Profile
        fields = ['code', 'first_name', 'last_name', 'email', 'phone', 'profile_type', 'about', 'username', 'password1', 'password2',]