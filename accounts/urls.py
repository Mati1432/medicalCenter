"""Urls files."""
# Django
from django.urls import include, re_path
from django.urls import path

# Project
from accounts import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path(r'patent-sign-up/', views.PatientSignUp.as_view(), name='patient-sign-up'),
    path(r'doctor-sign-up/', views.DoctorSignUp.as_view(), name='doctor-sign-up'),
]
