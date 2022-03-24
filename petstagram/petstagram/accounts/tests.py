import logging
from datetime import date

from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

from petstagram.accounts.models import Profile
from petstagram.main.models import Pet, PetPhoto

UserModel = get_user_model()


class ProfileDetailsViewTests(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        'username': 'testuser',
        'password': '12345qew',
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
        'picture': 'http://test.picture/url.png',
        'date_of_birth': date(1990, 4, 13),
    }

    VALID_PET_DATA = {
        'name': 'The pet',
        'type': Pet.CAT,
    }

    VALID_PET_PHOTO_DATA = {
        'photo': 'asd.jpg',
        'publication_date': date.today(),
    }

    def __create_user(self, **credentials):
        return UserModel.objects.create_user(**credentials)

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )

        return (user, profile)

    def __create_pet_and_pet_photo_for_user(self, user):
        pet = Pet.objects.create(
            **self.VALID_PET_DATA,
            user=user,
        )
        pet_photo = PetPhoto.objects.create(
            **self.VALID_PET_PHOTO_DATA,
            user=user,
        )
        pet_photo.tagged_pets.add(pet)
        pet_photo.save()
        return (pet, pet_photo)

    def __get_response_for_profile(self, profile):
        return self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))

    def test_when_opening_not_existing_profile__expect_404(self):
        response = self.client.get(reverse('profile details', kwargs={
            'pk': 1,
        }))

        self.assertEqual(404, response.status_code)

    def test_expect_correct_template(self):
        _, profile = self.__create_valid_user_and_profile()
        self.__get_response_for_profile(profile)
        self.assertTemplateUsed('accounts/profile_details.html')

    def test_when_user_is_owner__expect_is_owner_to_be_true(self):
        _, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)

        response = self.__get_response_for_profile(profile)

        self.assertTrue(response.context['is_owner'])

    def test_when_user_is_not_owner__expect_is_owner_to_be_false(self):
        _, profile = self.__create_valid_user_and_profile()
        credentials = {
            'username': 'testuser2',
            'password': '12345qwe',
        }

        self.__create_user(**credentials)

        self.client.login(**credentials)

        response = self.__get_response_for_profile(profile)

        self.assertFalse(response.context['is_owner'])

    def test_when_no_photo_likes__expect_total_likes_count_to_be_0(self):
        user, profile = self.__create_valid_user_and_profile()
        self.__create_pet_and_pet_photo_for_user(user)
        response = self.__get_response_for_profile(profile)

        self.assertEqual(0, response.context['total_likes_count'])

    def test_when_photo_likes__expect_total_likes_count_to_be_correct(self):
        likes = 3
        user, profile = self.__create_valid_user_and_profile()
        _, pet_photo = self.__create_pet_and_pet_photo_for_user(user)
        pet_photo.likes = likes
        pet_photo.save()

        response = self.__get_response_for_profile(profile)

        self.assertEqual(likes, response.context['total_likes_count'])

    def test_when_no_photos__no_photos_count(self):
        # same as likes
        pass

    def test_when_user_has_pets__expect_to_return_only_users_pets(self):
        user, profile = self.__create_valid_user_and_profile()
        credentials = {
            'username': 'testuser2',
            'password': '12345qwe',
        }
        user2 = self.__create_user(**credentials)

        pet, _ = self.__create_pet_and_pet_photo_for_user(user)
        # Create a pet/pets for different user
        self.__create_pet_and_pet_photo_for_user(user2)

        response = self.__get_response_for_profile(profile)

        self.assertListEqual(
            [pet],
            response.context['pets'],
        )

    def test_when_user_has_no_pets__pets_should_be_empty(self):
        _, profile = self.__create_valid_user_and_profile()

        response = self.__get_response_for_profile(profile)
        self.assertListEqual(
            [],
            response.context['pets'],
        )

    def test_when_no_pets__likes_and_photos_count_should_be_0(self):
        pass
