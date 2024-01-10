from django import forms
from  . import models

class Album_from(forms.ModelForm):
    class Meta:
        model = models.AlbumModel
        fields = '__all__'