from django import forms
from .models import albums

class albumForm(forms.ModelForm):
    class Meta:
        model = albums
        fields = '__all__'
        exclude = ['author']