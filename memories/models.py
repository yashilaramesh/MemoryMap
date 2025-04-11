from django.db import models
class Memory(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    date = models.IntegerField() #this should be models.DateField()
    description = models.TextField()
    #address = models.TextField()
    #visibility = models.Field.choices(['public','private'])
    #image = models.ImageField(upload_to='movie_images/')
    #also if memories can be "pinned" from business that should be a field
    def __str__(self):
        return str(self.id) + ' - ' + self.title
# Create your models here.
