from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.main.forms import CreatePetForm, EditPetForm, DeletePetForm


class CreatePetView(views.CreateView):
    template_name = 'main/pet_create.html'
    form_class = CreatePetForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditPetView(views.UpdateView):
    template_name = 'main/pet_edit.html'
    form_class = EditPetForm


class DeletePetView(views.DeleteView):
    template_name = 'main/pet_delete.html'
    form_class = DeletePetForm
