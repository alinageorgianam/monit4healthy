# m4h/admin.py

from django.contrib import admin
from .models import Patient, Appointment, Measurement, Prescription, BlackboxMedicalMeasurement, UricAcidMeasurement, GaitbandMeasurement, EmgMeasurement, Profile

admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Measurement)
admin.site.register(Prescription)
admin.site.register(BlackboxMedicalMeasurement)
admin.site.register(UricAcidMeasurement)
admin.site.register(GaitbandMeasurement)
admin.site.register(EmgMeasurement)
admin.site.register(Profile)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nume', 'prenume', 'email', 'role')
    search_fields = ('nume', 'prenume', 'email', 'role')
