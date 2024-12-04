# m4h/models.py

from django.contrib.auth.models import User

from django.contrib.auth.models import User
from django.db import models
from .utils import extract_cnp_info




class Profile(models.Model):
    """
         Represents a user profile in the system

         Attributes:
         user: A one-to-one relationship with a User object
         nume: A string representing the user's surname
         prenume: A string representing the user's first name
         cnp: A unique string representing the user's personal numerical code
         adresa: An optional string representing the user's address
         varsta: An optional integer representing the user's age
         telefon: An optional string representing the user's phone number
         email: A string representing the user's unique email address
         role: A string representing the user's role, which can be either 'doctor' or 'pacient'
         id_doctor: An optional foreign key to another Profile object, representing the user's doctor
         last_active: An optional datetime indicating when the user was last active

         Methods:
         __str__: Returns the username associated with this profile
         is_doctor: Checks if the user's role is 'doctor'
         is_pacient: Checks if the user's role is 'pacient'
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    cnp = models.CharField(max_length=13, unique=True, blank=True, null=True)
    adresa = models.CharField(max_length=255, null=True, blank=True)
    varsta = models.IntegerField(null=True, blank=True)
    telefon = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=[('doctor', 'Doctor'), ('pacient', 'Pacient')])
    id_doctor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='pacient')
    last_active = models.DateTimeField(null=True, blank=True)
    cod_parafa = models.CharField(max_length=6, null=True, blank=True)



    def __str__(self):
        return f'{self.user.username} Profile'

    #def __str__(self):
    #    return self.user.username

    @property
    def cnp_info(self):
        if not self.cnp:
            return {}
        try:
            return extract_cnp_info(self.cnp)
        except ValueError as e:
            return {"error": str(e)}

    @property
    def is_doctor(self):
        return self.role == 'doctor'

    @property
    def is_pacient(self):
        return self.role == 'pacient'

from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """
    Django signal receiver to create a user profile upon User creation.

    @param instance: The User instance that was created.
    @param created: Boolean indicating if a new User instance was created.

    If a new User instance was created, this function automatically
    creates a corresponding Profile instance for that User.
    """
    if created:
        profile = Profile.objects.create(
            user=instance,
            nume=getattr(instance, 'nume', ''),
            prenume=getattr(instance, 'prenume', ''),
            cnp=getattr(instance, 'cnp', ''),
            varsta=getattr(instance, 'varsta', ''),
            email=getattr(instance, 'email', ''),
            role=getattr(instance, 'role', ''),
            adresa=getattr(instance, 'adresa', ''),
            telefon=getattr(instance, 'telefon', ''),
            last_active=getattr(instance, 'last_active', ''),
            #cod_parafa=getattr(instance, 'cod_parafa', ''),
            #id_doctor_id=getattr(instance, 'id_doctor_id', '')
        )
        if profile.role == 'doctor':
            Doctor.objects.create(
                user=instance,
                nume=profile.nume,
                prenume=profile.prenume,
                cnp=profile.cnp,
                varsta=profile.varsta,
                email=profile.email,
                cod_parafa=profile.cod_parafa,
                adresa=profile.adresa,
                telefon=profile.telefon,
                last_active=profile.last_active,
            )
        elif profile.role == 'pacient':
            Patient.objects.create(
                user=instance,
                nume=profile.nume,
                prenume=profile.prenume,
                cnp=profile.cnp,
                varsta=profile.varsta,
                email=profile.email,
                adresa=profile.adresa,
                telefon=profile.telefon,
                id_doctor_id=profile.id_doctor_id,
                last_active=profile.last_active,
            )


@receiver(post_save, sender=User)
def save_user_profile(instance, **kwargs):
    """

    Handles the post-save signal for the User model, ensuring that the User's associated Profile is saved whenever the User instance is saved.

    @param instance: The instance of the User model that has been saved.
    """
    instance.profile.save()


class Patient(models.Model):
    """
        Represents a Patient entity in the database.

        Attributes:
            user (ForeignKey): A one-to-one relationship with the User model, which will be deleted on User deletion.
            doctor (ForeignKey): A foreign key relationship with the User model, representing the patient's doctor.
                                 The relationship will be set to null if the referenced User is deleted. It uses the
                                 related_name 'patients' to refer to the related objects.
            nume (CharField): The surname of the patient with a maximum length of 100 characters.
            prenume (CharField): The given name of the patient with a maximum length of 100 characters.
            varsta (IntegerField): The age of the patient as an integer.
            email (EmailField): The email address of the patient, with a default value of 'default@example.com'.

        Methods:
            __str__: Returns the full name of the patient in "nume prenume" format.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='patients')
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    varsta = models.IntegerField()
    email = models.EmailField(default='default@example.com')
    cnp = models.CharField(max_length=13, unique=True, null=True, blank=True)
    telefon = models.CharField(max_length=15, null=True, blank=True)
    adresa = models.CharField(max_length=255, null=True, blank=True)
    id_doctor_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='doctors')
    last_active = models.DateTimeField(null=True, blank=True)





    def __str__(self):
        return f"{self.nume} {self.prenume}"

class Doctor(models.Model):
    """
    Represents a Doctor model in the system. Each doctor is associated with a unique user and has attributes for name, surname, age, and email.

    Attributes:
        user (OneToOneField): The user associated with the doctor. If the user is deleted, the doctor entry is also deleted.
        nume (CharField): The doctor's last name with a maximum length of 100 characters.
        prenume (CharField): The doctor's first name with a maximum length of 100 characters.
        varsta (IntegerField): The doctor's age.
        email (EmailField): The doctor's email, defaults to 'default@example.com'.

    Methods:
        __str__(): Returns the string representation of the doctor, specifically their full name.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    varsta = models.IntegerField()
    email = models.EmailField(default='default@example.com')
    cod_parafa = models.CharField(max_length=6, null=True, blank=True, unique=True)
    cnp = models.CharField(max_length=13, unique=True, null=True, blank=True)
    adresa = models.CharField(max_length=255, null=True, blank=True)
    telefon = models.CharField(max_length=15, null=True, blank=True)
    last_active = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f"{self.nume} {self.prenume}"

class Appointment(models.Model):
    """
        Appointment model represents an appointment between a doctor and a patient.

        Attributes:
        doctor : ForeignKey
            A reference to the doctor (user) associated with the appointment.
        patient : ForeignKey
            A reference to the patient associated with the appointment.
        appointment_date : DateTimeField
            The date and time of the appointment.

        Methods:
        __str__():
            Returns a string representation of the appointment in the format: "PatientName - AppointmentDate".
    """
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_appointments')
    appointment_date = models.DateTimeField()

    def __str__(self):
        return f"{self.patient.nume} {self.patient.prenume} - {self.appointment_date}"


class Measurement(models.Model):
    """

    Measurement model class

    Attributes:
        patient: ForeignKey linking to the Patient model, representing the patient associated with the measurement.
        timestamp: DateTimeField indicating when the measurement was taken.
        uric_acid_level: FloatField representing the uric acid level measured.
        absorbance: FloatField representing the absorbance measured.

    Methods:
        __str__: Returns a string representation of the measurement, including the patient's name and the timestamp.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    uric_acid_level = models.FloatField()
    absorbance = models.FloatField()

    def __str__(self):
        return f"Measurement for {self.patient.nume} {self.patient.prenume} at {self.timestamp}"


class Prescription(models.Model):
    """

    Represents a medical prescription issued to a patient by a doctor.

    Attributes:
        patient (ForeignKey): Reference to the Patient model. When patient is deleted, corresponding Prescription is also deleted.
        doctor (ForeignKey): Reference to the User model representing the doctor. When doctor is deleted, corresponding Prescription is also deleted.
        date_issued (DateTimeField): Date and time when the prescription was issued.
        medication_name (CharField): Name of the prescribed medication, limited to 100 characters.
        dosage (CharField): Instructions on the amount of medication to take, limited to 100 characters.
        duration (CharField): Duration for which the medication should be taken, limited to 100 characters.
        quantity (IntegerField): Quantity of the medication prescribed.
        additional_info (TextField): Optional field for any additional information related to the prescription. Can be null or blank.

    Methods:
        __str__: Returns a string representation of the Prescription object, including the patient's name.
    """
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
    """
        A Django model representing a medical measurement recorded by a blackbox device.

        Attributes:
            patient (ForeignKey): A reference to the patient for whom the measurement is recorded. Deletes the measurement if the patient is deleted.
            timestamp (DateTimeField): The date and time the measurement was recorded.
            ekg (FloatField): The measured electrocardiogram (EKG) value.
            pulse (FloatField): The measured pulse value.
            spo2 (FloatField): The measured oxygen saturation (SpO2) value.
            temperature (FloatField): The measured body temperature value.
            co2 (FloatField): The measured carbon dioxide (CO2) level.
            alcoolemia (FloatField): The measured blood alcohol concentration.

        Methods:
            __str__(): Returns a string representation of the measurement with patient details and the timestamp.
    """
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
    """
    Defines the UricAcidMeasurement model which stores the uric acid measurement details for a patient.

    Attributes:
        patient: A ForeignKey linking to the Patient model. Represents the patient for whom the uric acid measurement is taken.
        timestamp: A DateTimeField indicating when the uric acid measurement was taken.
        uric_acid_level: A FloatField capturing the uric acid level in the patient's blood.
        absorbance: A FloatField noting the absorbance value during the uric acid measurement.

    Methods:
        __str__: Returns a string representation of the Uric Acid Measurement instance, including patient name and timestamp.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    uric_acid_level = models.FloatField()
    absorbance = models.FloatField()

    def __str__(self):
        return f"Uric Acid Measurement for {self.patient.nume} {self.patient.prenume} at {self.timestamp}"


class GaitbandMeasurement(models.Model):
    """
    GaitbandMeasurement model represents the measurements taken by a gait analysis device for a patient.

    Attributes:
        patient (ForeignKey): Reference to the patient the measurement belongs to.
        timestamp (DateTimeField): Date and time when the measurement was taken.
        fall_detected (BooleanField): Indicator whether a fall was detected during this measurement.

    Methods:
        __str__: Returns a string representation of the GaitbandMeasurement instance, detailing the patient's name and timestamp of the measurement.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    fall_detected = models.BooleanField()

    def __str__(self):
        return f"Gaitband Measurement for {self.patient.nume} {self.patient.prenume} at {self.timestamp}"


class EmgMeasurement(models.Model):
    """
        Represents an electromyography (EMG) measurement for a patient.

        Attributes:
            patient (ForeignKey): A reference to the patient for whom the measurement was taken.
            timestamp (DateTimeField): The date and time when the measurement was recorded.
            muscle_activity (FloatField): The recorded muscle activity level.

        Methods:
            __str__(): Returns a string representation of the EMG measurement including the patient's name and measurement timestamp.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    muscle_activity = models.FloatField()

    def __str__(self):
        return f"EMG Measurement for {self.patient.nume} {self.patient.prenume} at {self.timestamp}"
