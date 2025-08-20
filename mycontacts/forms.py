from django import forms
from .models import Contact

class AddForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('name', 'relation', 'phone', 'email',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'relation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Relation'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

