from django.shortcuts import render,redirect
from django.http  import HttpResponse 
import datetime as dt
from django.conf.urls.static import static
from.models import Image,Category,Location


# def welcome(request):
#     return render(request, 'All-pictures/home.html')

def images(request): 
    title = 'Home'
    images = Image.get_images()   
    return render(request, 'All-pictures/home.html', {'title':title, 'images':images})



def images_today(request):
    date = dt.date.today()
    return render(request, 'All-pictures/images-of-day.html', {"date": date,})

def past_days_images(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(images_of_day)

    return render(request, 'All-pictures/past-uploads.html', {"date": date})