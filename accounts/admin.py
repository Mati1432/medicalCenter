"""Admin files."""
# Django
from django.contrib import admin

# Project
from accounts.models import CustomUser
from accounts.models import UserInformation


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):  # noqa D101
    pass


@admin.register(UserInformation)
class UserInformationAdmin(admin.ModelAdmin):  # noqa D101
    pass
