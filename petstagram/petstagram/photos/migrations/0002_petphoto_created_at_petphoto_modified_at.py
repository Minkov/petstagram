# Generated by Django 4.2.9 on 2024-01-24 19:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("photos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="petphoto",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="petphoto",
            name="modified_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
