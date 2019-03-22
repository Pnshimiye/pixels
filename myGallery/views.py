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

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Image.search_image_category(search_term)
        message = f"{search_term}"

        return render(request, 'All-pictures/category.html',{"message":message,"images": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'All-pictures/category.html',{"message":message})

def location_search_results(request):

    if 'location' in request.GET and request.GET["location"]:
        search_term = request.GET.get("location")
        searched_location = Image.search_image_location(search_term)
        message = f"{search_term}"

        return render(request, 'All-pictures/location.html',{"message":message,"photos": searched_location})

    else:
        message = "You haven't searched for any term"
        return render(request, 'All-pictures/location.html',{"message":message})



# def location_search_results(request,location_id):
#     try:
#         location = Location.objects.get(id = location_id)
#     except DoesNotExist:
#         raise Http404()
#     return render(request,"All-pictures/location.html", {"location":location})

def location(request,location_id):  
    try: 
            # locations = Location.objects.all()
            location = Location.objects.get(id = location_id)
            images = Image.objects.filter(location = location.id)    
    except:        
            raise Http404()   
    return render(request,'All-pictures/location.html',{'location':location,'images':images,})





 
       