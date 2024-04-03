from petstagram.pets.models import Pet

PET_DATA = {
    "name": "TestPet",
    "pet_photo": "https://example.com/test.jpg",
    "date_of_birth": "2020-01-01"
}


def create_valid_pet(user):
    pet = Pet(
        **PET_DATA,
        user=user,
    )

    pet.save()

    return pet
