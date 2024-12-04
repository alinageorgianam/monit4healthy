# m4h/views.py
import json
from datetime import datetime, timezone

from django.contrib.auth import login, authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .forms import CustomUserCreationForm
from .models import Patient, Appointment, Prescription
from .models import Profile
from .utils import extract_cnp_info


@csrf_exempt
def login_view(request):
    """
    Handles user login requests.

    Accepts POST requests only. Expects the request to be in JSON format. Checks the content type of the request,
    parses the JSON data, and retrieves the username and password. Authenticates the user and logs them in if the
    credentials are correct. Returns a JSON response indicating the success or failure of the authentication.

    Parameters:
    request (HttpRequest): The HTTP request object containing the login data.

    Returns:
    JsonResponse: A JSON response indicating the success or failure of the login attempt.
    """
    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({'message': 'Autentificare reușită', 'success': True}, status=200)
            else:
                return JsonResponse({'message': 'Nume de utilizator sau parolă incorecte', 'success': False},
                                    status=400)
        else:
            return JsonResponse({'message': 'Invalid content type'}, status=400)

    return JsonResponse({'message': 'Doar cereri POST sunt permise'}, status=405)


from django.shortcuts import render


def profile_view(request):
    user_profile = request.user.profile
    cnp_info = {}

    if user_profile.cnp:
        try:
            cnp_info = extract_cnp_info(user_profile.cnp)
        except ValueError as e:
            cnp_info = {"error": str(e)}

    context = {
        'user': request.user,
        'cnp_info': cnp_info,
    }
    return render(request, 'Profiles\profil.html', context)




def logout_view(request):
    """
    Handles user logout process.

    This function logs out the current user and then redirects them to the login page.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: The redirection to the login page.
    """
    logout(request)
    return redirect('login')



@csrf_exempt
def register(request):
    """
    Handles user registration through both GET and POST requests.

    For POST requests:
    - Processes the registration form data.
    - If the data is valid, creates a new user and logs them in.
    - Returns a JsonResponse with a success message and HTTP status 201.
    - If the data is invalid, returns a JsonResponse with error details and HTTP status 400.

    For GET requests:
    - Renders the registration page with an empty form.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            backend = 'django.contrib.auth.backends.ModelBackend'
            auth_login(request, user, backend=backend)
            return JsonResponse({'message': 'Înregistrare reușită', 'success': True}, status=201)
        else:
            return JsonResponse({'message': 'Erori de validare', 'errors': form.errors, 'success': False}, status=400)
    else:
        form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})


@login_required(login_url='login')
def main(request):
    return render(request, 'MainTemplate/main.html', {'user': request.user})


def profil(request):
    return render(request, 'Profiles/profil.html')


def chat(request):
    return render(request, 'Chat&Video/chat.html')


def prescriptii(request):
    if request.user.profile.role == 'doctor':
        if request.method == 'POST':
            patient_id = request.POST.get('patient')

            print(f"Selected patient ID: {patient_id}")

            medication_name = request.POST.get('medication_name')
            dosage = request.POST.get('dosage')
            duration = request.POST.get('duration')
            quantity = request.POST.get('quantity')
            additional_info = request.POST.get('additional_info')

            try:
                patient = get_object_or_404(Patient, id=patient_id)
            except Patient.DoesNotExist:
                print(f"Patient with ID {patient_id} does not exist.")
                return redirect('prescriptii')

            Prescription.objects.create(
                patient=patient,
                doctor=request.user,
                date_issued=timezone.now(),
                medication_name=medication_name,
                dosage=dosage,
                duration=duration,
                quantity=quantity,
                additional_info=additional_info,
            )
            return redirect('prescriptii')

        patients = Profile.objects.filter(role='pacient')
        context = {
            'patients': patients,
        }

    elif request.user.profile.role == 'pacient':
        try:
            patient = Patient.objects.get(user=request.user)
            prescriptions = Prescription.objects.filter(patient=patient).order_by('-date_issued')
            context = {
                'prescriptions': prescriptions,
            }
        except Patient.DoesNotExist:
            context = {
                'error': 'Patient profile not found.',
            }

    return render(request, 'prescriptii.html', context)


def view_personal_history(request):
    return render(request, 'MedicalHistory/istoric_medical.html')


def view_patient_history(request):
    return render(request, 'MedicalHistory/istoric_medical_pacienti.html')


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
    return render(request, 'Appointments/programari.html', {'patients': patients, 'appointments': appointments})


@login_required
def view_patients(request):
    patients = Profile.objects.filter(role='pacient')
    monitored_patients = request.user.monitored_patients.all() if hasattr(request.user, 'monitored_patients') else []

    for patient in monitored_patients:
        if patient.last_active:
            time_difference = datetime.now(timezone.utc) - patient.last_active
            patient.is_online = time_difference.total_seconds() < 300
        else:
            patient.is_online = False

    context = {
        'patients': patients,
        'monitored_patients': monitored_patients,
    }
    return render(request, 'afisare_pacienti.html', context)


def main_view(request):
    if request.user.profile.role == 'doctor':
        # Fetch the profiles of the patients monitored by the doctor
        monitored_patients = Profile.objects.filter(role='pacient')

        context = {
            'monitored_patients': monitored_patients,
        }

    elif request.user.profile.role == 'pacient':
        # Code for handling the case when the user is a patient (unchanged)
        try:
            patient = Patient.objects.get(user=request.user)
            context = {
                'patient': patient,
            }
        except Patient.DoesNotExist:
            context = {
                'error': 'Patient profile not found.',
            }

    return render(request, 'main.html', context)




@login_required
def view_medical_results(request):
    patients = Patient.objects.filter(doctor=request.user)
    return render(request, 'Equipments&Systems/rez_med.html', {'patients': patients})


"""@login_required
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

"""


def get_appointments(request):
    return None


def get_patient_data(request):
    return None


def upload_image_patient(request):
    return None


def intro(request):
    return render(request, 'IntroPage/homepage.html')