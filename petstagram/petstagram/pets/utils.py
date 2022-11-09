from petstagram.pets.models import Pet


def get_pet_by_name_and_username(pet_slug, username):
    return Pet.objects \
        .filter(slug=pet_slug, user__username=username) \
        .get()
