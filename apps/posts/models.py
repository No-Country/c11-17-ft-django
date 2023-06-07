from django.db import models
from django.conf import settings

class Post(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts', null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    cost_hour = models.IntegerField(default=0)

    def __str__(self):
        return self.title
