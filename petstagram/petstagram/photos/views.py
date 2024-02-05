from django.shortcuts import render

from petstagram.photos.models import PetPhoto


def create_photo(request):
    context = {}
    return render(request, "photos/create_photo.html", context)


def details_photo(request, pk):
    context = {
        'pet_photo': PetPhoto.objects.get(pk=pk),
    }

    return render(request, "photos/details_photo.html", context)


def edit_photo(request, pk):
    context = {}

    return render(request, "photos/edit_photo.html", context)



