from django.db import models
class Memory(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    date = models.DateField(default = "2025-4-17")
    description = models.TextField(default="Memory")
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    visibility = models.BooleanField(default=False)
    image = models.ImageField(upload_to='memory_images/', default='memory_images/memory.jpg')
    def __str__(self):
        return str(self.id) + ' - ' + self.title
# Create your models here.