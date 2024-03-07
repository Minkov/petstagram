from django.shortcuts import render
from django.urls import reverse
from django.views import generic as views

from django.contrib.auth import mixins as auth_mixin

from petstagram.accounts.views import OwnerRequiredMixin
from petstagram.photos.forms import PetPhotoCreateForm, PetPhotoEditForm
from petstagram.photos.models import PetPhoto


class PetPhotoCreateView(auth_mixin.LoginRequiredMixin, views.CreateView):
    form_class = PetPhotoCreateForm
    template_name = "photos/create_photo.html"
    queryset = PetPhoto.objects.all() \
        .prefetch_related("pets")

    def get_success_url(self):
        return reverse("details photo", kwargs={
            "pk": self.object.pk,
        })

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.instance.user = self.request.user
        return form


class PetPhotoDetailView(auth_mixin.LoginRequiredMixin, views.DetailView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related("photolike_set") \
        .prefetch_related("photocomment_set") \
        .prefetch_related("pets")

    template_name = "photos/details_photo.html"


class PetPhotoEditView(OwnerRequiredMixin, auth_mixin.LoginRequiredMixin, views.UpdateView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related("pets")

    template_name = "photos/edit_photo.html"
    form_class = PetPhotoEditForm

    def get_success_url(self):
        return reverse("details photo", kwargs={
            "pk": self.object.pk,
        })
