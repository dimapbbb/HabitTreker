from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.create(
            email="superuser@mail.com",
            password=make_password('zxcdfrt56'),
            is_superuser=True,
            is_staff=True,
        )