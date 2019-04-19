from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

# User = get_user_model()


class Message(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    text = models.TextField(default='')
    date = models.DateTimeField(default=timezone.now)
