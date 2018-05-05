from django.test import TestCase
from .models import Location,Category, Images
# Create your tests here.
class Category(TestCase):
    def setUp(self):
        self.cat = Category(category="categoryx")
class LocationTestClass(TestCase):
    def setUp(self):
        self.loc = Location(area="locationx")
    def test_instance(self):
        self.assertTrue(isinstance(self.loc, Location))


class ImageTestClass(TestCase):
    '''
   image = models.ImageField(upload_to = 'articles/', blank=True)
    image_url = models.TextField(blank=True)
    image_name = models.CharField(max_length=30, blank=True)
    image_description = models.CharField(max_length=120,blank= True)
    category = models.ManyToManyField(Category,blank=True)
    location = models.ForeignKey('Location')
    post_date = models.DateTimeField(auto_now=True)

    
    models to test
    '''
    def setUp(self):
        self.images = Images(image_name='image', image_description='party at the beach',image_url="urlx",)
        self.images.save_editor()
    
    def teardown(self):
        Images.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()
    
