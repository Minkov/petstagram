from django.contrib.auth import get_user_model
from django.db import models
from petstagram.photos.models import Photo

# Create your models here.
"""
The field Comment Text is required:
• Comment Text - it should consist of a maximum of 300 characters
An additional field should be created:
• Date and Time of Publication - when a comment is created (only), the date of publication is automatically
generated
"""

UserModel = get_user_model()


class Comment(models.Model):
    comment_text = models.TextField(max_length=300, blank=False, null=False)
    # optional
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE, )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        ordering = ('-date_time_of_publication',)


class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )

    # CASCADE - delete 1 photo and delete all connected comments
    # RESTRICT/PROTECT - delete 1 photo ONLY if no connected comments
    # SET_NULL - delete 1 photo, set null for FK at comments, null=True
    # SET_DEFAULT
