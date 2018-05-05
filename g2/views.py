from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'g2/index.html')

def present(request):
    return render(request, 'g2/present.html')