# Generated by Django 4.2.9 on 2024-03-07 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("photos", "0005_alter_petphoto_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="petphoto",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.RESTRICT,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
