from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from models import Patient, Appointment


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1',
                  'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)

        if commit:
            user.is_active = False
            user.save()

        return user


class PatientRegistrationForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['pesel', 'address']

    def save(self, user, commit=True):
        patient = super(PatientRegistrationForm, self).save(commit=False)
        patient.user = user

        if commit:
            patient.save()

        return patient


class AppointmentReservationForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['clinic', 'doctor', 'date', 'start']

    def save(self, patient, commit=True):
        appointment = super(AppointmentReservationForm, self).save(commit=False)
        appointment.patient = patient

        if commit:
            appointment.save()

        return appointment
