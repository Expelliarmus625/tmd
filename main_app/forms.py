from django import forms
from accounts.models import ImageCollector

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageCollector
        fields = ['name', 'patient_img', 'username']
        widgets = {'username' : forms.HiddenInput()}