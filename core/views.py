"""Views files."""
# Django
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

# 3rd-party
from core.forms import VisitForm


class VisitView(FormView):  # noqa  D101
    template_name = 'visit.html'
    form_class = VisitForm
    success_url = reverse_lazy('')
