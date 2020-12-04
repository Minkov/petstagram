from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    profile_picture = models.ImageField(
        upload_to='users',
        blank=True
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
