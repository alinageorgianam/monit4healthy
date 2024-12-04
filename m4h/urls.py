from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.intro, name='intro'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('main/', views.main, name='main'),  # Aceasta linie redirecționează rădăcina către index
    path('profil/', views.profil, name='profil'),
    path('chat/', views.chat, name='chat'),
    path('view_personal_history/', views.view_personal_history, name='view_personal_history'),
    path('view_patient_history/', views.view_patient_history, name='view_patient_history'),
    path('upload_image/', views.upload_image_patient, name='upload_image_patient'),
    path('prescriptii/', views.prescriptii, name='prescriptii'),
    path('appointments/', views.manage_appointments, name='manage_appointments'),
    path('patients/', views.view_patients, name='view_patients'),
    path('medical_results/', views.view_medical_results, name='view_medical_results'),
    path('get_patient_data/<int:patient_id>/', views.get_patient_data, name='get_patient_data'),
    path('get_appointments/', views.get_appointments, name='get_appointments'),
]
