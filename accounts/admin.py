"""Admin files."""
# Django
from django.contrib import admin

# 3rd-party
from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):  # noqa D101
    pass
