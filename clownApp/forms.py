from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class AppointmentForm(forms.Form):
    appointment_date = forms.DateField(widget=DateInput)


class AppointmentModelForm(forms.Form):
    class Meta:
        widget = {'appointment_date': DateInput()}
