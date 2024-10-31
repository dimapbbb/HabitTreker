from datetime import timedelta

import requests

from config.settings import TG_TOKEN


def send_reminder_to_tg(habit):
    url = f'https://api.telegram.org/bot{TG_TOKEN}/sendMessage'
    params = {
        "text": str(habit),
        "chat_id": habit.user.tg_chat_id
    }
    response = requests.get(url, params=params)

    habit.next_send_date += timedelta(days=habit.periodicity)
    habit.save()