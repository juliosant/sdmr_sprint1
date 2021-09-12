from .models import CustomerService
from django import forms

class SearchRCForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Buscar por endereço, nome ou código'}))


class CustomerServiceForm(forms.ModelForm):
    STATUS_CONFIRMED = [
        (True, 'Sim'),
        (False, 'Não')
        
    ]

    confirmed = forms.ChoiceField(choices=STATUS_CONFIRMED)
    class Meta:
        model = CustomerService
        fields = '__all__'
