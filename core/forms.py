"""Forms files."""
from core.models import Visit


class VisitForm(forms.ModelForm):  # noqa D101

    class Meta:  # noqa D106
        model = Visit
        fields = [
            'doctor',
            'specialization',
            'date_visit',
            'visit',
        ]

