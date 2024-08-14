import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monit4healthy.settings')
django.setup()

from django.contrib.auth.models import User
from m4h.models import Profile

users = User.objects.all()

for user in users:
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user, nume=user.username, prenume='', role='pacient')
        print(f'Created profile for user {user.username}')

print('Profiles created for all users without profiles.')
