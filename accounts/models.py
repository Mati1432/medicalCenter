"""Models files."""
# Django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):  # noqa: D101

    phone = models.CharField(_('Phone'), max_length=15)
    pesel = models.CharField(_('Pesel'), max_length=11)
    birth_date = models.DateField(_('Birth Date'), null=True)
    email = models.EmailField(_('Email'), max_length=254)
    city = models.CharField(_('City'), max_length=254)
    street = models.CharField(_('Street'), max_length=254)

    class Meta:  # noqa: D106

        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):  # noqa: D105
        return f'{self.email} {self.last_name} {self.pesel}'
