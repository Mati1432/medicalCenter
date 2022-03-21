"""Urls files."""
# Django
from django.template.defaulttags import url
from django.urls import include
from django.urls import path

from accounts import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path(r'^patent-sign-up/', views.PatientSignUp.as_view(), name='patient-sign-up'),
    path(r'^doctor-sign-up/', views.DoctorSignUp.as_view(), name='doctor-sign-up'),
]
