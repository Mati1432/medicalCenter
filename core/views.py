"""Views files."""
from django.urls import reverse_lazy

from core.forms import VisitForm


class VisitView(FormView):  # noqa  D101
    template_name = 'visit.html'
    form_class = VisitForm
    success_url = reverse_lazy('')

