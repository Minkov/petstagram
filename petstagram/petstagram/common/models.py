from django.contrib.auth import get_user_model
from django.db import models

from petstagram.photos.models import PetPhoto

UserModel = get_user_model()


class PhotoComment(models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.TextField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,  # Done only on `create`
    )

    modified_at = models.DateTimeField(
        auto_now=True,  # On every save
    )

    pet_photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.RESTRICT,
    )

    user = models.ForeignKey(UserModel,
                             on_delete=models.RESTRICT)


class PhotoLike(models.Model):
    pet_photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.RESTRICT,
    )

    user = models.ForeignKey(UserModel,
                             on_delete=models.RESTRICT)

# photo_like = PhotoLike.objects \
#         .filter(pet_photo_id=pet_photo.pk, user=request.user)
