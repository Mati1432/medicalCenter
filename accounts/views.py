"""Views files."""

# Django
from django.shortcuts import render

from allauth.account.views import SignupView

from .forms import SignUpForm
from .forms import DoctorSignUpForm


class PatientSignUp(SignupView):
    template_name = 'signup_patient.html'
    form_class = SignUpForm
    redirect_field_name = 'next'
    view_name = 'patient_sign_up'

    def get_context_data(self, **kwargs):
        ret = super(PatientSignUp, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret


class DoctorSignUp(SignupView):
    template_name = 'signup_doctor.html'
    form_class = DoctorSignUpForm
    redirect_field_name = 'next'
    view_name = 'candidate_sign_up'

    def get_context_data(self, **kwargs):
        ret = super(DoctorSignUp, self).get_context_data(**kwargs)
        print(ret)
        ret.update(self.kwargs)
        return ret
