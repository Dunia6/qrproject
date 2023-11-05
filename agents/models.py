from django.db import models

# Create your models here.

class Agent(models.Model):
    """ Class Agent """
    thumbnail = models.ImageField(upload_to='agents/', null=True, blank=True)
    name = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    
    def __Str__(self):
        return self.name