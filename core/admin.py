"""Admin files."""
# Django
from django.contrib import admin

# 3rd-party
from core.models import Visit


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):  # noqa D101
    pass
