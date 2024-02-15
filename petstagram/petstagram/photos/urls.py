from django.urls import path, include

from petstagram.photos.views import PetPhotoCreateView, PetPhotoEditView, PetPhotoDetailView

urlpatterns = (
    path("create/", PetPhotoCreateView.as_view(), name="create photo"),
    path(
        "<int:pk>/",
        include([
            path("", PetPhotoDetailView.as_view(), name="details photo"),
            path("edit/", PetPhotoEditView.as_view(), name="edit photo"),
        ]),
    ),
)
