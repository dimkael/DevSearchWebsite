from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=User)
def on_user_created(sender, instance, created, **kwargs):
    user = instance

    if created:
        Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )


@receiver(post_save, sender=Profile)
def on_profile_updated(sender, instance, created, **kwargs):
    profile = instance
    user = None
    try:
        user = profile.user
    except:
        pass

    if user and not created:
        if profile.name:
            user.first_name = profile.name
        if profile.username:
            user.username = profile.username
        if profile.email:
            user.email = profile.email
        user.save()


@receiver(post_delete, sender=Profile)
def on_profile_deleted(sender, instance, **kwargs):
    user = None
    try:
        user = instance.user
    except:
        pass

    if user:
        user.delete()