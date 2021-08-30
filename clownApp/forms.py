from django import forms
from .models import Appointment, Clown


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['clown', 'client', 'activity']


class ClownForm(forms.ModelForm):
    class Meta:
        model = Clown
        fields = ['clown', 'price', 'status']