from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
import datetime, random

# Classes
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    text = models.TextField()
    cover = models.ImageField(upload_to='imagens/')
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Contact(models.Model):
    
    name = models.CharField(max_length=255)
    email = models.EmailField()
    desc = models.TextField()
    
class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='imagens/')

    timestamp = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp"]