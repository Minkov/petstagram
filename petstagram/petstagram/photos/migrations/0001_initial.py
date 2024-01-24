# Generated by Django 4.2.9 on 2024-01-24 19:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("pets", "0002_alter_pet_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="PetPhoto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("photo", models.ImageField(upload_to="pet_photos/")),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        max_length=300,
                        null=True,
                        validators=[django.core.validators.MinLengthValidator(10)],
                    ),
                ),
                ("location", models.CharField(blank=True, max_length=30, null=True)),
                ("pets", models.ManyToManyField(to="pets.pet")),
            ],
        ),
    ]
