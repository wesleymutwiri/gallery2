from django.db import models
import datetime as dt
# Create your models here.
class Category(models.Model):
    '''
    categories = people,nature, buildings, food
    '''
    name = models.CharField(max_length=50)
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    
    @classmethod
    def update_category(cls,id,location,update):
        updated = cls.objects.filter(id=id).update(category=update)
        return updated

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
    location = models.ForeignKey('Location')
    post_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-post_date']   
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete() 
    
    @classmethod
    def update_image(cls,id,target,update):
        updated = cls.objects.filter(id=id).update(target=update)
        return updated
    
    @classmethod
    def get_image(cls,id):
        files = cls.objects.get(id=id)
        return files

    @classmethod
    def search_by_image(cls,search_image):
        pics = cls.objects.filter(image_name__icontains=search_image)
        return pics
    
