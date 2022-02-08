import datetime

from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.main.validators import validate_only_letters, validate_file_max_size_in_mb


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]
    # ^ same as v
    # GENDERS = [
    #     ('Male', 'Male'),
    #     ('Female', 'Female'),
    #     ('Do not show', 'Do not show'),
    # ]

    # id/pk by default
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
            # always_valid('asd'),
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    picture = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    # Constants
    CAT = "Cat"
    DOG = "Dog"
    BUNNY = "Bunny"
    PARROT = "Parrot"
    FISH = "Fish"
    OTHER = "Other"

    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]
    # TYPES = ((x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)), not a tuple comprehension, generator
    NAME_MAX_LENGTH = 30

    # Fields(Columns)
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    # One-to-one relations

    # One-to-many relations
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    # Many-to-many relations

    # Properties

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    # Methods

    # dunder methods

    # Meta
    class Meta:
        unique_together = ('user_profile', 'name')


class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=(
            # validate_file_max_size_in_mb(5),
            # validate_file_max_size_in_mb(7),
            # validate_file_max_size_in_mb(8),
        )
    )
    tagged_pets = models.ManyToManyField(
        Pet,
        # validate at least 1 pet
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )

    # likes = models.ForeignKey(
    #     Like
    # )
