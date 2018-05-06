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
    def get_image_by_Id(cls, image_id):
      return cls.objects.get(pk=image_id)

   @classmethod
    def search_by_title(cls, search_term):
        img = cls.objects.filter(category__category__icontains=search_term)
        return img

    # @classmethod
    # def get_image_by_location(cls,location):
    #     images = cls.objects.filter(location__location_area__icontains=location).all()
    #     return images
    
   @classmethod
    def search_category(cls, categorys_name):
        return cls.objects.filter(category__category=categorys_name)
    
    @classmethod
    def filter_by_location(cls, location):
        return cls.objects.filter(location=location)



   