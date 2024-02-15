from django.urls import path, include


from petstagram.pets.views import PetCreateView, PetDetailView, PetDeleteView, PetEditView

urlpatterns = (
    path("create/", PetCreateView.as_view(), name="create pet"),
    path("<str:username>/pet/<slug:pet_slug>/",
         include([
             path("", PetDetailView.as_view(), name='details pet'),
             path("edit/", PetEditView.as_view(), name='edit pet'),
             path("delete/", PetDeleteView.as_view(), name='delete pet'),
         ])),
)
