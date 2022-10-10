from django.db import models

from petstagram.photos.models import Photo

'''
The field Comment Text is required:
    • Comment Text - it should consist of a maximum of 300 characters
An additional field should be created:
    • Date and Time of Publication - when a comment is created (only), the date of publication is automatically generated
'''


class PhotoComment(models.Model):
    MAX_TEXT_LENGTH = 300
    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )


class PhotoLike(models.Model):
    # Photo's field for likes is named `{NAME_OF_THIS_MODEL.lower()}_set`
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    # When we have users
    # user = models.ForeignKey(
    #     User
    # )
