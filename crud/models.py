from django.db import models

# Create your models here.
class PersonalDetails(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    number = models.CharField(max_length=10)
    address = models.CharField(max_length=255)

