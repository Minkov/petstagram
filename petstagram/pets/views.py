from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.accounts.decorators import user_required
from petstagram.core.clean_up import clean_up_files
from petstagram.pets.forms.comment_form import CommentForm
from petstagram.pets.forms.pet_form import PetForm
from petstagram.pets.models import Pet, Like, Comment


def list_pets(request):
    context = {
        'pets': Pet.objects.all(),
    }

    return render(request, 'pet_list.html', context)


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


def persist_pet(request, pet, template_name):
    if request.method == 'GET':
        form = PetForm(instance=pet)

        context = {
            'form': form,
            'pet': pet,
        }

        return render(request, f'{template_name}.html', context)
    else:
        old_image = pet.image
        form = PetForm(
            request.POST,
            request.FILES,
            instance=pet
        )
        if form.is_valid():
            if old_image:
                clean_up_files(old_image.path)
            form.save()
            Like.objects.filter(pet_id=pet.id) \
                .delete()
            return redirect('pet details or comment', pet.pk)

        context = {
            'form': form,
            'pet': pet,
        }

        return render(request, f'{template_name}.html', context)


@user_required(Pet)
def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    return persist_pet(request, pet, 'pet_edit')


@login_required
def create_pet(request):
    pet = Pet()
    return persist_pet(request, pet, 'pet_create')


@login_required
def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if pet.user.user != request.user:
        # forbid
        pass
    if request.method == 'GET':
        context = {
            'pet': pet,
        }

        return render(request, 'pet_delete.html', context)
    else:
        pet.delete()
        return redirect('list pets')


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


# Long, non-reusable variants of create and edit
def edit_pet_long(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        form = PetForm(instance=pet)

        context = {
            'form': form,
            'pet': pet,
        }

        return render(request, 'pet_edit.html', context)
    else:
        form = PetForm(
            request.POST,
            instance=pet
        )
        if form.is_valid():
            form.save()
            return redirect('pet details or comment', pet.pk)

        context = {
            'form': form,
            'pet': pet,
        }

        return render(request, f'pet_edit.html', context)


def create_pet_long(request):
    if request.method == 'GET':
        form = PetForm()

        context = {
            'form': form,
        }

        return render(request, 'pet_create.html', context)
    else:
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save()
            return redirect('pet details or comment', pet.pk)

        context = {
            'form': form,
        }

        return render(request, f'pet_edit.html', context)
