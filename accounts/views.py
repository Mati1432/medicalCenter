"""Views files."""

# 3rd-party
from allauth.account.views import SignupView

# Local
from .forms import DoctorSignUpForm
from .forms import SignUpForm


class PatientSignUp(SignupView):  # noqa D101
    template_name = 'signup_patient.html'
    form_class = SignUpForm
    redirect_field_name = 'next'
    view_name = 'patient_sign_up'

    def get_context_data(self, **kwargs):  # noqa D102
        ret = super(PatientSignUp, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret


class DoctorSignUp(SignupView):  # noqa D101
    template_name = 'signup_doctor.html'
    form_class = DoctorSignUpForm
    redirect_field_name = 'next'
    view_name = 'doctor_sign_up'

    def get_context_data(self, **kwargs):  # noqa D102
        ret = super(DoctorSignUp, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret
