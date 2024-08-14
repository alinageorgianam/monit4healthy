# m4h/models.py

# models.py

from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    cnp = models.CharField(max_length=13, unique=True)
    adresa = models.CharField(max_length=255, null=True, blank=True)
    varsta = models.IntegerField(null=True, blank=True)
    telefon = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=[('doctor', 'Doctor'), ('pacient', 'Pacient')])
    id_doctor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='pacient')
    last_active = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def __str__(self):
        return self.user.username

    @property
    def is_doctor(self):
        return self.role == 'doctor'

    @property
    def is_pacient(self):
        return self.role == 'pacient'

# Pentru a crea automat un Profile când un utilizator este creat
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='patients')
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    varsta = models.IntegerField()
    email = models.EmailField(default='default@example.com')

    def __str__(self):
        return f"{self.nume} {self.prenume}"


class Appointment(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_appointments')
    appointment_date = models.DateTimeField()

    def __str__(self):
        return f"{self.patient.nume} {self.patient.prenume} - {self.appointment_date}"

class Measurement(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    uric_acid_level = models.FloatField()
    absorbance = models.FloatField()

    def __str__(self):
        return f"Measurement for {self.patient.nume} {self.patient.prenume} at {self.timestamp}"

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    date_issued = models.DateTimeField()
    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    quantity = models.IntegerField()
    additional_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Prescription for {self.patient.nume} {self.patient.prenume}"

class BlackboxMedicalMeasurement(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    ekg = models.FloatField()
    pulse = models.FloatField()
    spo2 = models.FloatField()
    temperature = models.FloatField()
    co2 = models.FloatField()
    alcoolemia = models.FloatField()

    def __str__(self):
        return f"Blackbox Measurement for {self.patient.nume} {self.patient.prenume} at {self.timestamp}"

class UricAcidMeasurement(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    uric_acid_level = models.FloatField()
    absorbance = models.FloatField()

    def __str__(self):
        return f"Uric Acid Measurement for {self.patient.nume} {self.patient.prenume} at {self.timestamp}"

class GaitbandMeasurement(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    fall_detected = models.BooleanField()

    def __str__(self):
        return f"Gaitband Measurement for {self.patient.nume} {self.patient.prenume} at {self.timestamp}"

class EmgMeasurement(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    muscle_activity = models.FloatField()

    def __str__(self):
        return f"EMG Measurement for {self.patient.nume} {self.patient.prenume} at {self.timestamp}"
