# monit4healthy/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('m4h.urls')),  # Include the app's URL configurations
    path('accounts/', include('django.contrib.auth.urls')),  # Add this line
]
