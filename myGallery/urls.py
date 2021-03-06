
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    url(r'^$',views.images,name='images'),         
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_images,name = 'pastuploads'),    
    url(r'^search/', views.search_results, name='search_results'),
    # url(r'^search_location/', views.location_search_results, name='location_search_results'),
    url(r'^location/(\d+)',views.location,name='location'),
  
  
 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)