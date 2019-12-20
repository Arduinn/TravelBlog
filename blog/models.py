from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime

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
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default='')
    desc = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name 
