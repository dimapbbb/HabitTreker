from rest_framework.test import APITestCase
from rest_framework import status

from users.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="test@mail.com",
            password="test_password"
        )
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        user_data = {
            "email": "tester@mail.com",
            "password": "test_password"
        }
        url = '/register/'

        response = self.client.post(url, data=user_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.all().exists())

    def test_update_user(self):
        url = f'/update_user/{self.user.pk}/'
        new_data = {
            "first_name": "test_name"
        }

        response = self.client.patch(url, data=new_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["first_name"], new_data["first_name"])

        new_auth_user = User.objects.create(
            email="tester@mial.com",
            password="tester_password"
        )

        self.client.force_authenticate(user=new_auth_user)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_user(self):
        url = f"/user/{self.user.pk}/"

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["email"], self.user.email)

        new_user = User.objects.create(
            email="tester@mial.com",
            password="tester_password"
        )

        self.client.force_authenticate(user=new_user)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_destroy_user(self):
        url = f'/delete_user/{self.user.pk}/'

        response = self.client.delete(url)

        delete_user = User.objects.get(id=self.user.pk)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(delete_user.is_active)
        self.assertTrue(User.objects.filter(id=self.user.pk).exists())


    def test_get_user_list(self):
        url = '/users/'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.user.is_staff = True

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


