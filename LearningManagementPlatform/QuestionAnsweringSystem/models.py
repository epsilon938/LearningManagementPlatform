from django.db import models

# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    roll_number = models.BigIntegerField(primary_key=True)
    phone_number = models.BigIntegerField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

