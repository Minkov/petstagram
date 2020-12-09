from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.decorators import user_required
from petstagram.core.clean_up import clean_up_files
from petstagram.pets.forms.comment_form import CommentForm
from petstagram.pets.forms.pet_form import PetForm
from petstagram.pets.models import Pet, Like, Comment


class PetsListView(views.ListView):
    model = Pet
    template_name = 'pet_list.html'
    context_object_name = 'pets'


@login_required
def details_or_comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
            'form': CommentForm(),
            'can_delete': request.user == pet.user.user,
            'can_edit': request.user == pet.user.user,
            'can_like': request.user != pet.user.user,
            'has_liked': pet.like_set.filter(user_id=request.user.userprofile.id).exists(),
            'can_comment': request.user != pet.user.user,
        }

        return render(request, 'pet_detail.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.pet = pet
            comment.user = request.user.userprofile
            comment.save()
            return redirect('pet details or comment', pk)
        context = {
            'pet': pet,
            'form': form,
        }

        return render(request, 'pet_detail.html', context)


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


@login_required
def like_pet(request, pk):
    like = Like.objects.filter(user_id=request.user.userprofile.id, pet_id=pk).first()
    if like:
        like.delete()
    else:
        pet = Pet.objects.get(pk=pk)
        like = Like(test=str(pk), user=request.user.userprofile)
        like.pet = pet
        like.save()
    return redirect('pet details or comment', pk)
