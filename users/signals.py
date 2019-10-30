from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver # reciever is the function that gets the signal and preforms a relevant task
from users.models import Profile


@receiver(post_save, sender=User) # when a user is saved preform this function
def create_profile(sender, instance, created, **kwargs):
    if created: # if the user is created then create a profile instance for this user
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save() # save the profile when the user is saved