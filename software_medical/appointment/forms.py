from django import forms
from .models import Appoinment
from software_medical.doctors.models import Doctor
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import datetime
from django.contrib import messages

User = get_user_model()


class AppointmentForms(forms.ModelForm):
    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        empty_label="Select the Doctor Please",
    )
    time = forms.TimeField(
        widget=forms.TimeInput(format="%H:%M", attrs={"type": "time"})
    )
    date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))

    class Meta:
        model = Appoinment
        exclude = ("user",)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(AppointmentForms, self).__init__(*args, **kwargs)
        self.fields["doctor"].widget.attrs["class"] = "form-control"
        self.fields["time"].widget.attrs["type"] = "time"

    def save(self, *args, **kwargs):

        appointment = super(AppointmentForms, self).save(commit=False)
        appointment.user = self.user
        appointment.save()
        return appointment

    def clean(self):
        """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
        super(AppointmentForms, self).clean()
        date = self.cleaned_data.get("date")
        if date < datetime.date.today():
            self._errors["date"] = self.error_class(["Date must not be in past"])
        return self.cleaned_data

    # def clean_date(self):
    #     date = self.cleaned_data["date_of_birth"]
    #     if date < datetime.date.today():
    #         raise ValidationError("The date cannot be in the past!")
    #     return date
