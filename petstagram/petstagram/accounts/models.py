from enum import Enum

from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models


def validate_only_alphabetical(value):
    pass


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]


class ChoicesStringsMixin(ChoicesMixin):
    @classmethod
    def max_length(cls):
        return max(len(x.value) for x in cls) + 1


class Gender(ChoicesMixin, Enum):
    MALE = 1
    FEMALE = 2
    DO_NOT_SHOW = 3

# TODO: if enough time
class Gender2(models.Model):
    name = models.CharField(max_length=30)


class PetstagramUser(auth_models.AbstractUser):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_alphabetical,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_alphabetical,
        )
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.IntegerField(
        choices=Gender.choices(),
        # max_length=Gender.max_length(),
        default=Gender.DO_NOT_SHOW.value,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.username

    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)

        # Send email on successful register: Variant 2
        # Good enough, but there is a better option (signals)
        # send_mail....
        return result

b = 5