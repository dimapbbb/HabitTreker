from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from habit.models import Habit


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, attrs):
        reward = attrs.get('reward')
        related_habit = attrs.get('related_habit_id')
        time_complete = attrs.get('time_complete')
        pleasant = attrs.get('pleasant')
        periodicity = attrs.get('periodicity')

        if reward and related_habit:
            raise ValidationError("Нельзя одновременно сохранить вознаграждение и связаную привычку")

        if time_complete:
            if time_complete > 120:
                raise ValidationError("Время выполнения должно быть не больше 120 секунд")

        if related_habit:
            if related_habit not in [habit.pk for habit in Habit.objects.filter(pleasant=True)]:
                raise ValidationError("Связаная привычка не из приятных")

        if pleasant:
            if reward or related_habit:
                raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки")

        if periodicity:
            if periodicity > 7:
                raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней")

        return attrs