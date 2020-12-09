from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.core.clean_up import clean_up_files
from petstagram.pets.forms.comment_form import CommentForm
from petstagram.pets.forms.pet_form import PetForm
from petstagram.pets.models import Pet, Like


class PetsListView(views.ListView):
    model = Pet
    template_name = 'pet_list.html'
    context_object_name = 'pets'


class PetDetailsView(views.DetailView):
    model = Pet
    template_name = 'pet_detail.html'
    context_object_name = 'pet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = context[self.context_object_name]
        context['form'] = CommentForm()
        context['can_delete'] = self.request.user == pet.user.user
        context['can_edit'] = self.request.user == pet.user.user
        context['can_like'] = self.request.user != pet.user.user
        context['has_liked'] = pet.like_set.filter(user_id=self.request.user.userprofile.id).exists()
        context['can_comment'] = self.request.user != pet.user.user
        context['comments'] = list(pet.comment_set.all())

        return context


class LikePetView(views.View):
    def get(self, request, **kwargs):
        user_profile = request.user.userprofile
        pet = Pet.objects.get(pk=kwargs['pk'])

        like = pet.like_set.filter(user_id=user_profile.id).first()
        if like:
            like.delete()
        else:
            like = Like(
                user=user_profile,
                pet=pet,
                test='as'
            )
            like.save()

        return redirect('pet details', pet.id)


class CommentPetView(auth_mixins.LoginRequiredMixin, views.FormView):
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user.userprofile
        comment.pet = Pet.objects.get(pk=self.kwargs['pk'])
        comment.save()
        return redirect('pet details', self.kwargs['pk'])


class CreatePetView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'pet_create.html'
    model = Pet
    form_class = PetForm

    def get_success_url(self):
        url = reverse_lazy('pet details or comment', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user.userprofile
        pet.save()
        return super().form_valid(form)
        # return redirect('pet details or comment', pet.id)


class UpdatePetView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'pet_edit.html'
    model = Pet
    form_class = PetForm

    def get_success_url(self):
        url = reverse_lazy('pet details or comment', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        old_image = self.get_object().image
        if old_image:
            clean_up_files(old_image.path)
        return super().form_valid(form)


class DeletePetView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Pet
    template_name = 'pet_delete.html'
    success_url = reverse_lazy('list pets')

    def dispatch(self, request, *args, **kwargs):
        pet = self.get_object()
        if pet.user_id != request.user.userprofile.id:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
