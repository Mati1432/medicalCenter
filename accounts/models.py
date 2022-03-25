"""Models files."""
# Django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from .consts import SPECIALIZATION


class CustomUser(AbstractUser):  # noqa: D101
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)


class UserInformation(models.Model):  # noqa: D101

    phone = models.CharField(_('Phone'), max_length=9, null=True, blank=True)
    pesel = models.CharField(_('Pesel'), max_length=11, null=True, blank=True)
    birth_date = models.DateField(_('Birth Date'), null=True, blank=True)
    email = models.EmailField(_('Email'), max_length=254, null=True, blank=True)
    city = models.CharField(_('City'), max_length=254, null=True, blank=True)
    street = models.CharField(_('Street'), max_length=254, null=True, blank=True)
    specialization = models.CharField(
        _('Specialization'),
        max_length=150,
        choices=SPECIALIZATION,
        null=True,
        blank=True,
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    class Meta:  # noqa: D106

        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):  # noqa: D105
        return f'{self.email}{self.user}'
