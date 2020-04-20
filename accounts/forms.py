from django import forms
from .models import patient_data

class PatientDataForm(forms.Form):
    class Meta:
        model = patient_data
        fields = ('name', 'ultrasound')