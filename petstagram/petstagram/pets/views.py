from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.core import exceptions

from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin

from petstagram.accounts.views import OwnerRequiredMixin
from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


class PetCreateView(auth_mixin.LoginRequiredMixin, views.CreateView):
    # `model` and `fields` in `CreateView` are only needed to
    # create a form with `modelform_factory`

    # model = Pet
    # fields = ("name", "date_of_birth", "pet_photo")

    form_class = PetCreateForm
    template_name = "pets/create_pet.html"

    def get_success_url(self):
        return reverse("details pet", kwargs={
            "username": "Doncho",
            "pet_slug": self.object.slug,
        })

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.instance.user = self.request.user
        return form


class PetEditView(OwnerRequiredMixin, views.UpdateView):
    model = Pet  # queryset = Pet.objects.all()
    form_class = PetEditForm
    template_name = "pets/edit_pet.html"

    slug_url_kwarg = "pet_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["username"] = "Doncho"
        return context

    def get_success_url(self):
        return reverse("details pet", kwargs={
            "username": self.request.GET.get("username"),
            "pet_slug": self.object.slug,
        })


class PetDetailView(auth_mixin.LoginRequiredMixin, views.DetailView):
    # TODO: fix bad queries
    # model = Pet  # or `queryset`
    queryset = Pet.objects.all() \
        .prefetch_related("petphoto_set") \
        .prefetch_related("petphoto_set__photolike_set") \
        .prefetch_related("petphoto_set__pets")

    template_name = "pets/details_pet.html"
    # slug_field = "pet_slug" # name of field in Model
    slug_url_kwarg = "pet_slug"  # name of param in URL


class PetDeleteView(OwnerRequiredMixin, auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = Pet
    form_class = PetDeleteForm

    template_name = "pets/delete_pet.html"

    slug_url_kwarg = "pet_slug"

    success_url = reverse_lazy("index")

    extra_context = {
        "username": "Doncho",
    }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs
