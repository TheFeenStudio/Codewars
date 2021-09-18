from django.db import models


class MailBox(models.Model):
    FIO = models.CharField(max_length=50)
    email = models.EmailField()