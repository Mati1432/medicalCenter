"""Models files."""
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Project
from accounts.models import CustomUser


class Visit(models.Model):  # noqa D101
    doctor = models.CharField(max_length=245)
    specialization = models.CharField(max_length=245)
    date_visit = models.DateTimeField()
    visit = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:  # noqa: D106

        verbose_name = _('Visit')
        verbose_name_plural = _('Visits')

    def __str__(self):  # noqa: D105
        return f'{self.doctor} {self.date_visit}'
