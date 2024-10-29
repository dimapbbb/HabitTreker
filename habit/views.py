from rest_framework import viewsets

from habit.models import Habit
from habit.pagination import Pagination
from habit.serializers import HabitSerializer
from users.models import User


class HabitViewSet(viewsets.ModelViewSet):
    """
    ВьюСет для работы с привычками
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = Pagination

    def perform_create(self, serializer):
        serializer.save(
            user=User.objects.get(id=1)
        )

    def get(self, request):
        paginated_queryset = self.paginate_queryset(self.queryset)
        serializer = self.serializer_class(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)
