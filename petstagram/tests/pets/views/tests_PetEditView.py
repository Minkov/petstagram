from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.helpers.pet_helpers import create_valid_pet
from tests.test_base import TestBase

UserModel = get_user_model()


class PetEditViewTests(TestBase):
    # logged_in_not_owner

    def test_get_edit__when_owner__expect_200_with_correct_pet_and_template(self):
        user = self._create_user()
        pet = create_valid_pet(user)

        self.client.login(**self.USER_DATA)
        response = self.client.get(
            reverse("edit pet", kwargs={
                "username": self.USER_DATA["email"],
                "pet_slug": pet.slug,
            }),
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pets/edit_pet.html")

    def test_post_edit__when_owner__expect_302_with_correct_redirect_and_edited_pet_with_unchanged_slug(self):
        pass

    def test_get_edit__when_anonymous__expect_302_with_redirect_to_login(self):
        user = self._create_user()
        pet = create_valid_pet(user)

        edit_pet_url = reverse("edit pet", kwargs={
                "username": self.USER_DATA["email"],
                "pet_slug": pet.slug,
            })

        response = self.client.get(edit_pet_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            f'{reverse("signin user")}?next={edit_pet_url}',
        )

    def test_get_edit__when_not_owner__expect_302_with_redirect_to_home(self):
        # Created with `self.USER_DATA`
        user = self._create_user()
        pet = create_valid_pet(UserModel.objects.create_user(
            email=self.USER_DATA["email"] + "2",
            password=self.USER_DATA["password"],
        ))

        self.client.login(**self.USER_DATA)

        response = self.client.get(
            reverse("edit pet", kwargs={
                "username": self.USER_DATA["email"],
                "pet_slug": pet.slug,
            }),
        )

        self.assertEqual(response.status_code, 403)

    def test_post_edit__when_not_owner__expect_302_with_redirect_to_home(self):
        pass
