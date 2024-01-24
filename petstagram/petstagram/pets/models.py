from django.db import models
from django.utils.text import slugify

'''
Open the pets/models.py file. There should be created one more field that will be auto populated with the following information:
•	Slug - a slug automatically generated using the pet's name and the pet's id, separated by a "-" (dash).
The slug is part of the URL and as you know each URL should be unique: 
'''


class Pet(models.Model):
    MAX_NAME_LENGTH = 30

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
    )

    pet_photo = models.URLField(
        null=False,
        blank=False,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        editable=False,  # Readonly, only in the Django App, not in the DB
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:  # slugify("My name") -> "My-name"
            self.slug = slugify(f"{self.name}-{self.pk}")

        super().save(*args, **kwargs)
