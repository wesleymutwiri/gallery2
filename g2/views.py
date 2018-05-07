from django.shortcuts import render,get_object_or_404
from .models import Images, Category, Location
import datetime as dt

# Create your views here.

def index(request):
    date=dt.date.today
    image = Images.objects.all()
    return render(request, 'g2/index.html', {"date":date, "image":image})

def present(request, image_id):
    image = Images.get_image_by_id(image_id)
    return render(request, 'g2/present.html', {"image":image})

def search_images(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Images.search_by_title(search_term)
        print(searched_images)
        message = f"{search_term}"

        return render(request, 'g2/search.html', {"message": message, "searched_images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'g2/search.html',{"message":message})

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
def details(request, image_id):
    image = get_object_or_404(Images, pk=image_id)
    return render(request, 'g2/details.html', {'image': image})