from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    phone = models.CharField(max_length=10, default='', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
