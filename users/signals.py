from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=User)
def on_profile_created(sender, instance, created, **kwargs):
    user = instance

    if created:
        Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )
    else:
        try:
            profile = Profile.objects.get(username=user.username)
            if profile:
                profile.name = user.first_name
                profile.email = user.email
                profile.save()
        except:
            pass


@receiver(post_delete, sender=Profile)
def on_profile_deleted(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass
