# Generated by Django 4.2.9 on 2024-02-15 16:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0002_alter_pet_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="pet_photo",
            field=models.URLField(max_length=500),
        ),
    ]