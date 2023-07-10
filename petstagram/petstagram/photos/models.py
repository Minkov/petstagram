# photos app - models
from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinLengthValidator
from .validators import image_size_validator_5mb, text_underscore_validator

from petstagram.pets.models import Pet

# Create your models here.

"""
The field Photo is required:
• Photo - the user can upload a picture from storage, the maximum size of the photo can be 5MB
The fields description and tagged pets are optional:
• Description - a user can write any description of the photo;
 it should consist of a maximum of 300 characters
and a minimum of 10 characters
• Location - it should consist of a maximum of 30 characters
• Tagged Pets - the user can tag none, one, or many of all pets.
 There is no limit on the number of tagged pets
There should be created one more field that will be automatically generated:
• Date of publication - when a picture is added or edited,
 the date of publication is automatically generated
"""

UserModel = get_user_model()


class Photo(models.Model):
    pet_image = models.ImageField(
        blank=False,
        null=False,
        validators=(image_size_validator_5mb,),
        upload_to="photos"
    )
    # optional
    description = models.TextField(
        max_length=300,
        validators=(MinLengthValidator(10), text_underscore_validator,),
        blank=True,
        null=True
    )
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return f"{self.pk} - {self.pet_image}"
