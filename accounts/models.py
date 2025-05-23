from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    securityQ1 = models.CharField(max_length=250)
    securityQ2 = models.CharField(max_length=250)
    securityA1 = models.CharField(max_length=250)
    securityA2 = models.CharField(max_length=250)
    business = models.BooleanField(default=False)
    def __str__(self):
        return self.username