"""Models files."""
# Django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .consts import specialization


class CustomUser(AbstractUser):  # noqa: D101
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)


class Doctor(models.Model):  # noqa: D101
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(_('Phone'), max_length=9)
    email = models.EmailField(_('Email'), max_length=254)
    city = models.CharField(_('City'), max_length=254)
    street = models.CharField(_('Street'), max_length=254)
    specialization = models.CharField(_('Specialization'), max_length=150, choices=specialization)


class Patient(models.Model):  # noqa: D101
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(_('Phone'), max_length=9)
    pesel = models.CharField(_('Pesel'), max_length=11)
    birth_date = models.DateField(_('Birth Date'), null=True)
    email = models.EmailField(_('Email'), max_length=254)
    city = models.CharField(_('City'), max_length=254)
    street = models.CharField(_('Street'), max_length=254)
    specialization = models.CharField(_('Specialization'), max_length=150, choices=specialization)

    class Meta:  # noqa: D106

        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):  # noqa: D105
        return f'{self.email} {self.pesel}'
