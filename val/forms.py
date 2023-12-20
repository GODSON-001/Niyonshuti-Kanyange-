# validationApp/forms.py
from django import forms
from .models import Participant, Vehicle
from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type':'date'}),
            }

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        widgets = {
            'manufacture_date': forms.DateInput(attrs={'type':'date'}),
        }
