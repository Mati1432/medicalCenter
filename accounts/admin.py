"""Admin files."""
# Django
from django.contrib import admin

# 3rd-party
from accounts.models import CustomUser, Doctor


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):  # noqa D101
    pass


@admin.register(Doctor)
class CustomUserAdmin(admin.ModelAdmin):  # noqa D101
    pass
