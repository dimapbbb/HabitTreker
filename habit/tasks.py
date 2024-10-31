from datetime import datetime

from celery import shared_task

from habit.models import Habit
from habit.services import send_reminder_to_tg


@shared_task
def search_reminder():
    habits = Habit.objects.filter(next_send_date=datetime.now().date())
    now_time = str(datetime.now().time())

    if habits:
        for habit in habits:
            time_to_send = str(habit.time)

            if now_time[:5] == time_to_send[:5]:
                send_reminder_to_tg(habit)
