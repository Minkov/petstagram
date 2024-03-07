from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from petstagram.accounts.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    # created = False, when update
    # create = True, when create
    if not created:
        return

    # Eager save
    Profile.objects.create(user=instance)
    # same as:
    # profile = Profile(user=instance)
    # Can run other code
    # profile.save()

