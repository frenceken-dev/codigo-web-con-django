from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone
from datetime import timedelta

    
    
# Otros modelos...


class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def is_valid(self):  # Valido por una Hora.
        return timezone.now() < self.create_at + timedelta(hours=1)
    
    def __str__(self):
        return f"token de {self.user.username}"