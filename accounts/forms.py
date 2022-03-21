# Django
from django import forms
from django.utils.translation import gettext_lazy as _

# 3rd-party
from accounts.consts import specialization
from accounts.models import CustomUser, Doctor, Patient
from allauth.account.forms import SignupForm


class SignUpForm(SignupForm):  # noqa D101
    first_name = forms.CharField(label=_('First name'), max_length=100)
    last_name = forms.CharField(label=_('Last name'), max_length=100)
    pesel = forms.CharField(label=_('Pesel'), max_length=100)
    birth_date = forms.CharField(label=_('Birth Date'), max_length=100)
    city = forms.CharField(label=_('City'), max_length=150)
    street = forms.CharField(label=_('Street'), max_length=150)
    phone = forms.CharField(label=_('Phone'), max_length=150)

    def save(self, request):  # noqa D102
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        pesel = self.cleaned_data['pesel']
        city = self.cleaned_data['city']
        birth_date = self.cleaned_data['birth_date']
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        street = self.cleaned_data['street']

        user = super().save(request)
        user.is_patient = True
        user.first_name = first_name
        user.last_name = last_name
        user.pesel = pesel
        user.city = city
        user.birth_date = birth_date
        user.email = email
        user.phone = phone
        user.street = street
        user.save()

        return user


class DoctorSignUpForm(SignupForm):  # noqa D101
    first_name = forms.CharField(label=_('First name'), max_length=100)
    last_name = forms.CharField(label=_('Last name'), max_length=100)
    city = forms.CharField(label=_('City'), max_length=150)
    street = forms.CharField(label=_('Street'), max_length=150)
    phone = forms.CharField(label=_('Phone'), max_length=150)
    specialization = forms.ChoiceField(choices=specialization)

    def save(self, request):  # noqa D102
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        city = self.cleaned_data['city']
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        street = self.cleaned_data['street']
        specialization = self.cleaned_data['specialization']

        user = super().save(request)
        user.first_name = first_name
        user.last_name = last_name
        user.city = city
        user.email = email
        user.phone = phone
        user.street = street
        user.specialization = specialization
        user.is_doctor = True
        user.save()

        return user
