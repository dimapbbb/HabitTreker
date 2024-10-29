from rest_framework import viewsets

from habit.models import Habit
from habit.serializers import HabitSerializer
from users.models import User


class HabitViewSet(viewsets.ModelViewSet):
    """
    ВьюСет для работы с привычками
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        serializer.save(
            user=User.objects.get(id=1)
        )
