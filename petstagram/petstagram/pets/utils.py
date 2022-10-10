from petstagram.pets.models import Pet


def get_pet_by_name_and_username(pet_slug, username):
    # TODO: fix `username` when auth
    return Pet.objects.get(slug=pet_slug)
