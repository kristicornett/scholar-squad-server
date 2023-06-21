from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Message(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    subject = models.CharField(max_length=200)
    body = models.TextField(max_length=2000)
    sent_date = models.DateTimeField(default=timezone.now)
    read_date = models.DateTimeField(blank=True, null=True)