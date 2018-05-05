from django.contrib import admin
from .models import Images, Location, Category
# Register your models here.
class ImagesAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)
admin.site.register(Location)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Category)