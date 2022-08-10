from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    clas = models.CharField(max_length=50)
    division = models.CharField(max_length=300)
    sc_name = models.CharField(max_length=100)