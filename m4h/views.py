# m4h/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, Appointment, Measurement, Prescription
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm  
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from .forms import EmailAuthenticationForm
from .models import Profile
from datetime import datetime, timezone

def login_view(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = EmailAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Specifică backend-ul explicit
            backend = 'django.contrib.auth.backends.ModelBackend'
            auth_login(request, user, backend=backend)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html', {'user': request.user})

def profil(request):
    return render(request, 'profil.html')


def chat(request):
    return render(request, 'chat.html')

def prescriptii(request):
    return render(request, 'prescriptii.html')

def view_personal_history(request):
    return render(request, 'istoric_medical.html')

def view_patient_history(request):
    return render(request, 'istoric_medical_pacienti.html')

def upload_image_patient(request):
    # Logica pentru încărcarea imaginii
    return render(request, 'numele_template.html')

@login_required
def manage_appointments(request):
    if request.method == 'POST':
        patient_id = request.POST['patient']
        appointment_date = request.POST['appointment_date']
        Appointment.objects.create(
            doctor=request.user,
            patient_id=patient_id,
            appointment_date=appointment_date
        )
    patients = Patient.objects.filter(doctor=request.user)
    appointments = Appointment.objects.filter(doctor=request.user)
    return render(request, 'programari.html', {'patients': patients, 'appointments': appointments})

@login_required
def view_patients(request):
    patients = Profile.objects.filter(role='pacient')
    monitored_patients = request.user.monitored_patients.all() if hasattr(request.user, 'monitored_patients') else []

    # Calculăm statusul fiecărui pacient (online/offline)
    for patient in monitored_patients:
        if patient.last_active:
            # Calculăm timpul scurs de la ultima activitate
            time_difference = datetime.now(timezone.utc) - patient.last_active
            # Verificăm dacă este mai mic de 300 de secunde (5 minute)
            patient.is_online = time_difference.total_seconds() < 300
        else:
            patient.is_online = False

    context = {
        'patients': patients,
        'monitored_patients': monitored_patients,
    }
    return render(request, 'afisare_pacienti.html', context)

@login_required
def view_medical_results(request):
    patients = Patient.objects.filter(doctor=request.user)
    return render(request, 'rez_med.html', {'patients': patients})

@login_required
def get_patient_data(request, patient_id):
    blackbox_measurements = BlackboxMedicalMeasurement.objects.filter(patient_id=patient_id)
    uric_acid_measurements = UricAcidMeasurement.objects.filter(patient_id=patient_id)
    gaitband_measurements = GaitbandMeasurement.objects.filter(patient_id=patient_id)
    emg_measurements = EmgMeasurement.objects.filter(patient_id=patient_id)
    return JsonResponse({
        'blackbox_measurements': list(blackbox_measurements.values()),
        'uric_acid_measurements': list(uric_acid_measurements.values()),
        'gaitband_measurements': list(gaitband_measurements.values()),
        'emg_measurements': list(emg_measurements.values())
    })

@login_required
def get_appointments(request):
    start = request.GET.get('start')
    end = request.GET.get('end')

    if request.user.profile.role == 'doctor':
        # Afișează programările tuturor pacienților pentru acest doctor
        appointments = Appointment.objects.filter(doctor=request.user, appointment_date__range=[start, end])
    elif request.user.profile.role == 'pacient':
        # Afișează programările doar pentru acest pacient
        appointments = Appointment.objects.filter(patient=request.user, appointment_date__range=[start, end])
    else:
        appointments = []

    # Continuă cu restul codului pentru a returna programările

