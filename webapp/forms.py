from django import forms
from webapp.models import Beer

class BeerForm(forms.ModelForm):
    class Meta:
        model = Beer
        fields = '__all__'
        widgets = {
            'creation': forms.TextInput(attrs={'type':'date','class':'date-class'})
        }