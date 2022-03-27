"""Urls Files."""
# Django
from django.urls import path

# 3rd-party
from core.views import VisitView

app_name = 'core'

urlpatterns = [
    path('visit/', (VisitView.as_view()), name='random'),
]
