from django import forms
from webapp.models import Beer

class BeerForm(forms.ModelForm):
    class Meta:
        model = Beer
        fields = '__all__'