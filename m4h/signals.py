from .models import Profile

def create_or_update_user_profile(instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
    else:
        try:
            instance.profile.save()
        except Profile.DoesNotExist:
            Profile.objects.create(user=instance)
