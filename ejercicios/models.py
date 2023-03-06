from django.db import models
import datetime

# Create your models here.
class Ejercicios(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image1 = models.ImageField(upload_to='ejercicios/images')
    image2 = models.ImageField(upload_to='ejercicios/images')
    date = models.DateField(datetime.date.today)