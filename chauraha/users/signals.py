from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver 
from .models import Profile




# basically we are binding the signal to the function using receiver decorator
#post_save is a signal which is fired when a model instance is saved
# sender = Guy who is creating the model instance

@receiver(post_save, sender= settings.AUTH_USER_MODEL,)
def create_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)

@receiver(post_save, sender= settings.AUTH_USER_MODEL)
def save_profile(sender, instance, **kwargs):
  instance.profile.save() 