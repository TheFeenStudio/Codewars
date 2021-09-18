from django.core.mail import send_mail
from .celery import app
from .models import MailBox


@app.task
def send_spam_email():
    for mail in MailBox.objects.all():
            send_mail(
                'Руки Вверх! Он тебя целует',
                'А он тебя целует, говорит что любит И ночами обнимает, к сердцу прижимает А я мучаюсь от боли со своей любовью Фотографии в альбоме о тебе напомнят А он тебя целует, говорит что любит И ночами обнимает, к сердцу прижимает А я мучаюсь от боли со своей любовью Фотографии в альбоме о тебе напомнят https://www.youtube.com/watch?v=phxQFEH51SE',
                'mbannakov13@gmail.com',
                [mail.email],
                fail_silently=False,
            )
#python3 manage.py runserver
#celery -A app worker -l info
#celery -A app beat -l info