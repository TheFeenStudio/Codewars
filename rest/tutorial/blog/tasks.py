from .celery import app
from .services import send
from celery import Celery

@app.task
def send_spam_email(user_email):
    send(user_email)
