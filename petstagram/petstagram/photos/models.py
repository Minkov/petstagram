from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, BaseValidator
from django.db import models

from petstagram.pets.models import Pet

UserModel = get_user_model()


def random_validator(value):
    # If invalid, `raise ValidationError`
    # Else, if valid, do nothing
    pass


SIZE_5_MB = 5 * 1024 * 1024


class MaxFileSizeValidator(BaseValidator):
    def clean(self, x):
        return x.size

    def compare(self, file_size, max_size):
        return max_size < file_size


def validate_image_size_less_than_5mb(value):
    # invalid:
    if value.size > SIZE_5_MB:
        raise ValidationError('File size should be less than 5MB')
    # valid:
    # do nothing


class PetPhoto(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='pet_photos/',
        blank=False,
        null=False,
        validators=(
            # validate_image_size_less_than_5mb,
            MaxFileSizeValidator(limit_value=SIZE_5_MB),
        )
    )

    description = models.TextField(
        blank=True,
        null=True,
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        )
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,  # Done only on `create`
    )

    modified_at = models.DateTimeField(
        auto_now=True,  # On every save
    )

    pets = models.ManyToManyField(Pet)

    user = models.ForeignKey(UserModel,
                             on_delete=models.RESTRICT)
