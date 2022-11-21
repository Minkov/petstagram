from datetime import date

from petstagram.common.models import PhotoLike
from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


def create_pets_for_user(user, count=5):
    result = [Pet(
        name=f'Pet {i + 1}',
        personal_photo=f'https://pets.com/{i + 1}.jpg',
        date_of_birth=date(2015 + i, (1 + i) % 12, (1 + i) % 28),
        user=user
    ) for i in range(count)]

    [p.save() for p in result]

    return result


def create_photo_for_user_and_pets(user, pets, count=5):
    photos = [Photo(
        photo=f'/var/images/img-{i + 1}.png',
        user=user,
    ) for i in range(count)]

    for photo in photos:
        photo.save()
        for pet in pets:
            photo.tagged_pets.add(pet)
        photo.save()

    return photos


def create_photo_likes_for_user_and_photos(user, photos):
    current = 0
    total_likes_count = 0

    for photo in photos:
        for i in range(current):
            PhotoLike(
                photo=photo,
                user=user
            ).save()

            total_likes_count += 1
        current += 1
    return total_likes_count
