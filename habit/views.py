from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit
from habit.pagination import Pagination

from habit.serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    """
    ВьюСет для работы с привычками
    """
    serializer_class = HabitSerializer
    pagination_class = Pagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )

    def get(self, request):
        paginated_queryset = self.paginate_queryset(self.queryset)
        serializer = self.serializer_class(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class PublicHabitListAPIView(generics.ListAPIView):
    queryset = Habit.objects.filter(public=True)
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination
