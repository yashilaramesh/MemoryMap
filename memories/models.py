from django.db import models
from django.conf import settings

class Memory(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    is_public = models.BooleanField(default=False)
    business_label = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='memory_images/', default='memory_images/memory.jpg')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f"{self.title} ({'Business' if self.is_public else 'Private'})"
