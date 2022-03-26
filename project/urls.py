"""Urls files."""
# Django
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    re_path(r'^rosetta/', include('rosetta.urls')),
]
urlpatterns += i18n_patterns(
    path('', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
)
