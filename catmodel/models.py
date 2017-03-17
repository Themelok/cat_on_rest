from django.db import models


# Create your models here.
class Breed(models.Model):
    breed = models.CharField(max_length=50)
    color = models.CharField(max_length=50)


class Cat(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed)
