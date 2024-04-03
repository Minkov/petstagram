from django.urls import reverse

from tests.helpers.pet_helpers import create_valid_pet, PET_DATA
from tests.helpers.pet_photo_helpers import create_valid_pet_photo
from tests.test_base import TestBase


class IndexViewTests(TestBase):
    def test_get_index__when_no_pets__expect_200_and_empty_object_list_in_context(self):
        response = self.client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/index.html")
        self.assertListEmpty(response.context["object_list"])

    def test_get_index__when_pets__expect_200_and_single_pet_in_context(self):
        # Arrange
        user = self._create_user()
        pet = create_valid_pet(user)
        photo = create_valid_pet_photo(user, pet)

        # Act
        response = self.client.get(reverse("index"))

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/index.html")
        self.assertListEqual([photo], list(response.context["object_list"]))
