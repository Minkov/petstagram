from petstagram.photos.models import PetPhoto

PET_PHOTOS_DATA = {
    "photo": "photo.jpg",
    "description": "Test description",
    "location": "Sofia",
}


def create_valid_pet_photo(user, pets):
    photo = PetPhoto(
        **PET_PHOTOS_DATA,
        user=user,
    )

    photo.save()
    photo.pets.add(pets)
    photo.save()

    return photo
