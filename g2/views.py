from django.shortcuts import render
from .models import Images, Category, Location
import datetime as dt

# Create your views here.

def index(request):
    date=dt.date.today
    image = Images.get_all_images()
    return render(request, 'g2/index.html', {"date":date, "image":image})

def present(request, image_id):
    image = Images.get_image_by_id(image_id)
    return render(request, 'g2/present.html', {"image":image})

def search_images(request):
    if 'image' in request.GET and request.GET["image"]:
        write = request.GET.get("image")
        found = Images.search_by_image(write)
        message = f"{write}"
        return render(request,'g2/search.html',{"message":message,"found":found})
    
    else:
        message = "No search image found within the database"
        return render(request,'g2/search.html',{"message":message})

        