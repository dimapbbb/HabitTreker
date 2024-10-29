from django.db import models

from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')

    place = models.CharField(max_length=100, verbose_name="Место")
    time = models.TimeField(verbose_name="Время напоминаия")
    action = models.CharField(max_length=500, verbose_name="Действие")

    pleasant = models.BooleanField(verbose_name="Признак приятной привычки")
    periodicity = models.PositiveSmallIntegerField(verbose_name="Периодичность в днях", default=1)
    public = models.BooleanField(verbose_name="Признак публичности", default=False)
    time_to_complete = models.TimeField(verbose_name="Длительность выполнения", blank=True, null=True)

    reward = models.CharField(max_length=200, verbose_name="Вознаграждение", blank=True, null=True)
    # or
    related_habit_id = models.PositiveIntegerField(verbose_name="пк связанной привычки", blank=True, null=True)

    def __str__(self):
        return f" Я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
