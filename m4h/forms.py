from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    nume = forms.CharField(max_length=100)
    prenume = forms.CharField(max_length=100)
    cnp = forms.CharField(max_length=13)
    adresa = forms.CharField(max_length=255)
    varsta = forms.IntegerField()
    telefon = forms.CharField(max_length=15)
    role = forms.ChoiceField(choices=[('doctor', 'Doctor'), ('pacient', 'Pacient')])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'nume', 'prenume', 'cnp', 'adresa', 'varsta', 'telefon', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()

            # Obține sau creează profilul utilizatorului
            profile, created = Profile.objects.get_or_create(user=user)
            
            # Actualizează câmpurile profilului
            profile.nume = self.cleaned_data.get('nume', '')
            profile.prenume = self.cleaned_data.get('prenume', '')
            profile.cnp = self.cleaned_data.get('cnp', '')
            profile.adresa = self.cleaned_data.get('adresa', '')
            profile.varsta = self.cleaned_data.get('varsta')
            profile.telefon = self.cleaned_data.get('telefon', '')
            profile.email = user.email
            profile.role = self.cleaned_data.get('role', '')

            # Salvează profilul
            profile.save()
        
        return user

    def clean_cnp(self):
        cnp = self.cleaned_data.get('cnp')
        if Profile.objects.filter(cnp=cnp).exists():
            raise forms.ValidationError("Acest CNP este deja înregistrat.")
        return cnp

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Profile.objects.filter(email=email).exists():
            raise forms.ValidationError("Acest email este deja utilizat.")
        return email


from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', max_length=254)

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("Utilizatorul cu acest email nu există.")
            
            self.confirm_login_allowed(user)

            if not user.check_password(password):
                raise forms.ValidationError("Parola este incorectă.")
            
            self.user_cache = user

        return self.cleaned_data
