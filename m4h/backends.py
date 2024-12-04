from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):
    """
    EmailBackend class that extends ModelBackend to authenticate users using their email and password.

    Parameters:
    request:
        The HTTP request object.
    username: str, optional
        The email of the user attempting to authenticate.
    password: str, optional
        The password of the user attempting to authenticate.
    kwargs: dict
        Additional keyword arguments.

    Returns:
        User object if authentication is successful, otherwise None.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        print(f"Authenticating with email: {username}")  # Verifică dacă metoda este apelată
        usermodel = get_user_model()
        try:
            user = usermodel.objects.get(email=username)
        except usermodel.DoesNotExist:
            print("User not found")
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            print("User authenticated")
            return user
        print("Password mismatch")
        return None
