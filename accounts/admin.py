"""Admin files."""
# Django
from django.contrib import admin

# 3rd-party
from accounts.models import CustomUser, Doctor, Patient


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):  # noqa D101
    pass
