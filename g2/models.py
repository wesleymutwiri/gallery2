from django.db import models
import datetime as dt
# Create your models here.
class Category(models.Model):
    '''
    categories = people,nature, buildings, food
    '''
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    
    @classmethod
    def update_category(cls,id,location,update):
        updated = cls.objects.filter(id=id).update(category=update)
        return updated
    
    
class Location(models.Model):
    area = models.CharField(max_length=50)

    def __str__(self):
        return self.area

    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()   
    
    @classmethod
    def update_location(cls, id, location, update):
        updated = cls.objects.filter(id=id).update(location=update)
        return updated
    
   

class Images(models.Model):
    # image_url = models.CharField(max_length=100, blank=True)
    image_name = models.CharField(max_length=30, blank=True)
    image_description = models.CharField(max_length=120,blank= True)
    category = models.ManyToManyField(Category,blank=True)
    location = models.ForeignKey('Location',)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'articles/', blank=True)

    class Meta:
        ordering = ['-pub_date']   
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete() 
    
    @classmethod
    def update_image(cls,id,target,update):
        update = cls.objects.filter(id=id).update(target=update)
        return update
    
    @classmethod
    def get_all_images(cls):
        images = cls.objects.order_by('-pub_date')
        return images

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def search_by_image(cls,search_image):
        pics = cls.objects.filter(image_name__icontains=search_image)
        return pics
   