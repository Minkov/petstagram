# photos/models.py
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from cloudinary import models as cloudinary_models

from petstagram.core.model_mixins import StrFromFieldsMixin
from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_less_than_5mb

UserModel = get_user_model()


class Photo(StrFromFieldsMixin, models.Model):
    str_fields = ('pk', 'photo', 'location')
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    # Requires mediafiles to work correctly
    photo = cloudinary_models.CloudinaryField(
        null=False,
        blank=True,
        # validators=(validate_file_less_than_5mb,),
    )

    description = models.CharField(
        # DB validation
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            # Django/python validation, not DB validation
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )

    publication_date = models.DateField(
        # Automatically sets current date on `save` (update or create)
        auto_now=True,
        null=False,
        blank=True,
    )

    # One-to-one relations

    # One-to-many relations

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    # Many-to-many relations

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )
