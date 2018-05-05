from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'g2/index.html')

def present(request):
    image = Image.get_image(image_id)
    return render(request, 'g2/present.html', {"image":image})