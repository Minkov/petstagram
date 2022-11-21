from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from tests.accounts.BaseTestCase import TestCaseBase
from tests.utils.creation_utils import create_pets_for_user, create_photo_for_user_and_pets, \
    create_photo_likes_for_user_and_photos

UserModel = get_user_model()


class UserDetailsViewTests(TestCaseBase):
    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'test_user@petstagram.tk',
        'password': '12345qwe',
    }

    def test_user_details__when_owner__expect_is_owner_true(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertTrue(response.context['is_owner'])

    def test_user_details__when_not_owner__expect_is_owner_false(self):
        profile_user = self._create_user_and_login({
            'username': self.VALID_USER_DATA['username'] + '1',
            'email': self.VALID_USER_DATA['email'] + '1',
            'password': self.VALID_USER_DATA['password'],
        })

        self._create_user_and_login(self.VALID_USER_DATA)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': profile_user.pk}))

        self.assertFalse(response.context['is_owner'])

    def test_user_details__when_no_pets__expect_empty_pets(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEmpty(response.context['pets'])

    def test_user_details__when_pets_and_no_photo__expect_pets_and_no_photos(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        create_pets_for_user(user, count=5)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(5, len(response.context['pets']))
        self.assertEmpty(response.context['photos'])
        self.assertEqual(0, response.context['photos_count'])

    def test_user_details__when_pets_and_1_photo__expect_pets_1_photo(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        pets = create_pets_for_user(user, count=5)
        photos = create_photo_for_user_and_pets(user, pets=pets[:2], count=1)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(5, len(response.context['pets']))
        self.assertEqual(1, len(response.context['photos']))
        self.assertListEqual(list(photos), list(response.context['photos']))
        self.assertEqual(1, response.context['photos_count'])

    def test_user_details__when_pets_and_2_photos__expect_pets_2_photos(self):
        pass

    def test_user_details__when_pets_and_7_photos_no_page__expect_pets_7_photos(self):
        pass

    def test_user_details__when_pets_and_7_photos_page_1__expect_pets_7_photos(self):
        pass

    def test_user_details__when_pets_and_7_photos_page_2__expect_pets_7_photos(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        pets = create_pets_for_user(user, count=5)
        photos = create_photo_for_user_and_pets(user, pets=pets[:2], count=7)

        response = self.client.get(
            reverse_lazy('details user', kwargs={'pk': user.pk}),
            data={
                'page': 2,
            })

        self.assertListEqual(pets, list(response.context['pets']))
        self.assertListEqual(photos[2:4], list(response.context['photos']))
        self.assertEqual(7, response.context['photos_count'])

    def test_user_details__when_no_likes__expect_0_likes_count(self):
        pass

    def test_user_details__when_likes_for_single_pet__expect_correct_likes_count(self):
        pass

    def test_user_details__when_likes_for_multiple_pets__expect_combined_likes_count(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        pets = create_pets_for_user(user, count=5)
        photos = create_photo_for_user_and_pets(user, pets=pets[:2], count=7)
        total_likes_count = create_photo_likes_for_user_and_photos(user, photos)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(total_likes_count + 1, response.context['likes_count'])
