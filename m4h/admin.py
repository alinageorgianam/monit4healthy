# m4h/admin.py

from django.contrib import admin
from .models import Patient, Doctor, Appointment, Measurement, Prescription, BlackboxMedicalMeasurement, UricAcidMeasurement, GaitbandMeasurement, EmgMeasurement, Profile

admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Measurement)
admin.site.register(Prescription)
admin.site.register(BlackboxMedicalMeasurement)
admin.site.register(UricAcidMeasurement)
admin.site.register(GaitbandMeasurement)
admin.site.register(EmgMeasurement)
admin.site.register(Profile)
admin.site.register(Doctor)


class ProfileAdmin(admin.ModelAdmin):
    """
        ProfileAdmin is a customized admin interface for the Profile model.

        Attributes:
            list_display: A tuple containing the fields to be displayed in the list view of the admin interface.
            search_fields: A tuple containing the fields that can be searched in the admin interface.
    """
    list_display = ('user', 'nume', 'prenume', 'email', 'role')
    search_fields = ('nume', 'prenume', 'email', 'role')
