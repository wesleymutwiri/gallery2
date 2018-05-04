from django.db import models
import datetime as dt
# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Location(models.Model):
    location = models.CharField(max_length=50)
    def __str__(self):
        return self.location

class Images(models.Model):
    image = models.ImageField(upload_to = 'articles/', blank=True)
    image_url = models.TextField(blank=True)
    image_name = models.CharField(max_length=30, blank=True)
    image_description = models.CharField(max_length=120,blank= True)
    display_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category,blank=True)
    location = models.ForeignKey('Location')

    

