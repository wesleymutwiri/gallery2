from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns =[ 
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search_images, name = 'search_images'),
    # url(r'^description/', views.view_information, name = 'show'),
    url(r'^details/(?P<image_id>[0-9]+)/$', views.details, name='details'),
]    

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
