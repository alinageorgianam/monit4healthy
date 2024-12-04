from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .utils import extract_cnp_info

class CustomUserCreationForm(UserCreationForm):
    """

    CustomUserCreationForm is a custom form for creating a new user with additional fields.

    Attributes:
        nume (CharField): A character field for the user's last name with a max length of 100.
        prenume (CharField): A character field for the user's first name with a max length of 100.
        cnp (CharField): A character field for the user's CNP with a max length of 13.
        adresa (CharField): A character field for the user's address with a max length of 255.
        varsta (IntegerField): An integer field for the user's age.
        telefon (CharField): A character field for the user's phone number with a max length of 15.
        role (ChoiceField): A choice field for the user's role, either 'doctor' or 'pacient'.

    Meta:
        model (User): The model associated with this form.
        fields (list): List of fields to include in the form.

    Methods:
        save(commit=True): Saves the user instance with associated profile information.
            commit (bool): Optional. Whether to commit the changes to the database. Defaults to True.
            Returns:
                user: The user instance created.

        clean_cnp(): Validates the CNP field to ensure it is unique.
            Returns:
                cnp: The cleaned CNP value.
            Raises:
                forms.ValidationError: If the CNP already exists in the database.

        clean_email(): Validates the email field to ensure it is unique.
            Returns:
                email: The cleaned email value.
            Raises:
                forms.ValidationError: If the email already exists in the database.
    """
    nume = forms.CharField(max_length=100)
    prenume = forms.CharField(max_length=100)
    cnp = forms.CharField(max_length=13)
    adresa = forms.CharField(max_length=255)
    varsta = forms.CharField()
    telefon = forms.CharField(max_length=15)
    role = forms.ChoiceField(choices=[('doctor', 'Doctor'), ('pacient', 'Pacient')])
    cod_parafa=forms.CharField(max_length=6)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'nume', 'prenume', 'cnp', 'adresa', 'varsta', 'telefon', 'role', 'cod_parafa']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

            profile, created = Profile.objects.get_or_create(user=user)

            profile.nume = self.cleaned_data.get('nume', '')
            profile.prenume = self.cleaned_data.get('prenume', '')
            profile.cnp = self.cleaned_data.get('cnp', '')
            profile.adresa = self.cleaned_data.get('adresa', '')
            profile.varsta = self.cleaned_data.get('varsta')
            profile.telefon = self.cleaned_data.get('telefon', '')
            profile.email = user.email
            profile.role = self.cleaned_data.get('role', '')
            profile.cod_parafa=self.cleaned_data.get('cod_parafa', '')

            cnp_info = extract_cnp_info(profile.cnp)
            if cnp_info:
                profile.gender = cnp_info.get('gender')
                profile.zi_nastere = cnp_info.get('zi_nastere')
                profile.varsta = cnp_info.get('varsta')
                profile.judet = cnp_info.get('judet')
                profile.nr_unic = cnp_info.get('nr_unic')
                profile.cifra_control = cnp_info.get('cifra_control')


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

utilizator = get_user_model()

class EmailAuthenticationForm(AuthenticationForm):
    """

        A custom authentication form that uses email instead of a username for authentication.

        Attributes:
        username: A form field for the user's email address.

        Methods:
        clean(): Cleans and validates the form data. Checks if the user exists and if the password is correct.
    """
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
