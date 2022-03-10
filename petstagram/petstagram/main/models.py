import datetime

from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


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

    MIN_DATE = datetime.date(1920, 1, 1)

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
        validators=(
            # MinDateValidator(),
        )
    )

    # One-to-one relations

    # One-to-many relations
    user = models.ForeignKey(
        UserModel,
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
        unique_together = ('user', 'name')


class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=(
            # validate_file_max_size_in_mb(5),
            # validate_file_max_size_in_mb(7),
            # validate_file_max_size_in_mb(8),
        )
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

    tagged_pets = models.ManyToManyField(
        Pet,
        # validate at least 1 pet
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


'''
# Pet has a profile relation
SELECT *
FROM Pets p
JOIN Profiles pr
ON p.profile_id = pr.id
JOIN Users u
ON pr.user_id == u.id
WHERE u.id == request.user.id

# Pet has a user relation

SELECT *
FROM Pets p
JOIN Users u
ON p.user_id == u.id
WHERE u.id == request.user.id
'''
