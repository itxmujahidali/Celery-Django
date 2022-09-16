from django.contrib.auth import get_user_model
from celery_core.celery import app
from celery.schedules import crontab
from django.core.mail import send_mail


# Celery Beat Settings
app.conf.beat_schedule = {
    'send-mail at selected time': {
        'task': 'email_utils.task.sender_func',
        # 'schedule': crontab(hour=0, minute=40, day_of_month=19, month_of_year = 6),
        'schedule': crontab(hour=20, minute=11),
    }   
}

#TASK
@app.task(bind=True)
def sender_func(self):
    # send_mail(
    #     'Subject',
    #     'Message',
    #     'from@email.com',
    #     ['to@email.com'],
    #     fail_silently=False,
    #     )
    users = get_user_model().objects.all()
    for user in users:
        print('------>',user.email)
    return "Email Has Been Sent!"