from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.url = '/habits/'
        self.user = User.objects.create(email="tester@mail.com")
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            user=self.user,
            place="Home",
            time="20:00:00",
            action="Drink bear",
            pleasant=True
        )

    def test_list_habits(self):
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "pk": self.habit.pk,
                    "place": self.habit.place,
                    "time": self.habit.time,
                    "action": self.habit.action,
                    "pleasant": self.habit.pleasant,
                    "periodicity": 1,
                    "public": False,
                    "time_complete": None,
                    "reward": None,
                    "related_habit": None,
                    "owner": self.user.pk
                }
            ]
        }
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 1)
        self.assertEqual(response.json(), result)

    def test_delete_habit(self):
        response = self.client.delete(self.url + str(self.habit.pk) + "/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_update_habit(self):
        new_data = {
            "place": "kitchen",
            "time": "21:00",
            "action": "smoke sigar",
            "pleasant": False
        }
        response = self.client.patch(self.url + str(self.habit.pk) + "/", data=new_data)

        update_habit = Habit.objects.get(id=self.habit.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['place'], update_habit.place)
        self.assertEqual(response.json()['action'], update_habit.action)
        self.assertFalse(update_habit.pleasant)

    def test_retrieve_habit(self):
        response = self.client.get(self.url + str(self.habit.pk) + "/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['place'], self.habit.place)

    def test_create_habit(self):
        habit_data = {
            "place": "Home",
            "time": "20:00",
            "action": "Drink bear",
            "pleasant": True
        }

        response = self.client.post(self.url, data=habit_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['place'], habit_data['place'])
        self.assertTrue(Habit.objects.all().exists())

    def test_create_habit2(self):
        habit_data = {
            "place": "Home",
            "time": "20:00",
            "action": "Drink bear",
            "pleasant": True,
            "reward": "smoke sigar",
            "related_habit_id": 2
        }

        response = self.client.post(self.url, data=habit_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PublicHabitTestCase(APITestCase):

    def setUp(self):
        self.url = '/public_habits/'
        self.user = User.objects.create(email="tester@mail.com")
        self.client.force_authenticate(user=self.user)

        self.pub_habit = Habit.objects.create(
            user=self.user,
            place="Home",
            time="20:00:00",
            action="Drink bear",
            pleasant=True,
            public=True
        )
        self.not_pub_habit = Habit.objects.create(
            user=self.user,
            place="Home",
            time="20:00:00",
            action="Drink bear",
            pleasant=True,
            public=False
        )

    def test_get_public_habits_list(self):
        response = self.client.get(self.url)
        result = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {
                     'pk': self.pub_habit.pk,
                     'place': 'Home',
                     'time': '20:00:00',
                     'action': 'Drink bear',
                     'pleasant': True,
                     'periodicity': 1,
                     'public': True,
                     'time_complete': None,
                     'reward': None,
                     'related_habit': None,
                     'owner': 7
                }
            ]
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 2)
        self.assertEqual(response.json(), result)
