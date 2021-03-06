from .models import CustomerService, Donation, Material
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


class DonationForm(forms.ModelForm):
    STATUS_CONFIRMED = [
        (True, 'Sim'),
        (False, 'Não')        
    ]
    confirmed = forms.ChoiceField(choices=STATUS_CONFIRMED)
    class Meta:
        model = Donation
        fields = '__all__'


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'
        #widgets = {
        #    'points': forms.TextInput(attrs={'readonly':''})
        #}
