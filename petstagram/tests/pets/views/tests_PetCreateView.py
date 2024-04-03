from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify

from petstagram.pets.models import Pet
from tests.helpers.pet_helpers import PET_DATA
from tests.test_base import TestBase

UserModel = get_user_model()


class PetCreateViewTests(TestBase):

    def test_get_create__when_logged_in_user__expect_200_and_correct_template(self):
        # Arrange
        self._create_user()
        self.client.login(**self.USER_DATA)

        # Act
        response = self.client.get(reverse("create pet"))

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pets/create_pet.html")

    def test_get_create__when_anonymous_user__expect_302_with_redirect_to_login(self):
        create_pet_url = reverse("create pet")
        login_url = reverse("signin user")
        # Act
        response = self.client.get(create_pet_url)

        # Assert
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            f"{login_url}?next={create_pet_url}"
        )

    def test_post_create__when_logged_in_user__expect_302_with_correct_redirect_and_created_pet_with_correct_slug(self):
        # Arrange
        self._create_user()
        self.client.login(**self.USER_DATA)

        # Act
        response = self.client.post(
            reverse("create pet"),
            data=PET_DATA,
        )

        # Assert
        created_pet = Pet.objects.get(**PET_DATA)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse("details pet", kwargs={
                "username": self.USER_DATA["email"],
                "pet_slug": created_pet.slug,
            }),
        )

        self.assertEqual(
            slugify(f"{created_pet.name}-{created_pet.pk}"),
            created_pet.slug,
        )

    def test_post_create__when_anonymous_user__expect_302_with_redirect_to_login(self):
        create_pet_url = reverse("create pet")
        login_url = reverse("signin user")
        # Act
        response = self.client.post(
            create_pet_url,
            data=PET_DATA,
        )

        # Assert
        self.assertEqual(response.status_code, 302)
        self.assertEqual(f"{login_url}?next={create_pet_url}", response.url)
