from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print(f"Authenticating with email: {username}")  # Verifică dacă metoda este apelată
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            print("User not found")
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            print("User authenticated")
            return user
        print("Password mismatch")
        return None
