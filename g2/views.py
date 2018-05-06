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
        return render(request,'g2/search.html',{"message":message,"image":found})
    
    else:
        message = "No such image found within the database"
        return render(request,'g2/search.html',{"message":message})

def search_locations(request):
    if image in request.GET and request.GET["image"]:
        write = request.GET.get("image")
        found = Images.get_image_by_location(write)
        message = f"{write}"
        return render(request, 'g2/location.html',{"message":message,"found":found})

    else:
        message = "No such location found in the database "
        return render(request,'g2/location.html',{"message":message})

# def view_information(request):
#     show = Images.get_all_images()
#     return render(request, 'g2/images.html',{"date":date, "show":show })
        