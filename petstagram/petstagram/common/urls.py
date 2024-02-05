from django.urls import path

from petstagram.common.views import index, like_pet_photo

urlpatterns = (
    path("", index, name="index"),
    path("pet_photo_like/<int:pk>/", like_pet_photo, name="like_pet_photo"),
)
