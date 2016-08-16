from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Shout(models.Model):
    message = models.CharField(max_length=160)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['-created_at']
