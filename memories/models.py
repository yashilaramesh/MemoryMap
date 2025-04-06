from django.db import models
class Memory(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    date = models.IntegerField()
    description = models.TextField()
    #image = models.ImageField(upload_to='movie_images/')
    def __str__(self):
        return str(self.id) + ' - ' + self.title
# Create your models here.
