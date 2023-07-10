from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

"""
Name - it should consist of a maximum of 30 characters.
Personal Pet Photo - the user can link a picture using a URL
The field date of birth is optional:
• Date of Birth - pet's day, month, and year of birth

Slug - a slug automatically generated using the pet's
 name and the pet's id, separated by a "-" (dash
"""

UserModel = get_user_model()


class Pet(models.Model):
    name = models.CharField(max_length=30)
    personal_pet_photo = models.URLField()
    date_of_birth = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )

    def save(self, *args, **kwargs):
        # call parent save
        # this way, we will have an instance
        # CREATE
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")
        # UPDATE
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk} - {self.name}"
