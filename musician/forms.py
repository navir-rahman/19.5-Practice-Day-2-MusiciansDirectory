from django import forms
from .models import MusicianModel

class Musician_form(forms.ModelForm):
    class Meta:
        model = MusicianModel
        fields = '__all__'
        
