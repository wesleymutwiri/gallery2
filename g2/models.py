from django.db import models
import datetime as dt
# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.category

class Location(models.Model):
    location = models.CharField(max_length=50)
    
    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()   
    
    @classmethod
    def update_location(cls, id, location, update):
        updated = cls.objects.filter(id=id).update(location=update)
        return updated
    
    def __str__(self):
        return self.location

class Images(models.Model):
    image = models.ImageField(upload_to = 'articles/', blank=True)
    image_url = models.TextField(blank=True)
    image_name = models.CharField(max_length=30, blank=True)
    image_description = models.CharField(max_length=120,blank= True)
    category = models.ManyToManyField(Category,blank=True)
    post_date = models.DateTimeField(auto_now=True)
    location = models.ForeignKey('Location')

    class Meta:
        ordering = ['-post_date']   
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete() 


