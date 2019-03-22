from django.db import models
import datetime as dt




class Category(models.Model):
    category_name = models.CharField(max_length =30)

    def save_category(self):
      self.save()

    def delete_category(self):
      self.delete()

    def update_category(self):
      self.update()

    @classmethod
    def get_category_id(cls,id):
      category= Category.objects.get(id=id)
      return category
    

    

    def __str__(self):
        return self.category_name

class Location(models.Model):
    location_name = models.CharField(max_length =30)



    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self,new_location):
        self.location_name = new_location
        self.save()

    @classmethod
    def get_locations(cls):
        all_locations = Location.objects.all()
        return all_locations


    @classmethod
    def get_location_id(cls,id):
      location= Location.objects.get(id=id)
      return location 
        

    def __str__(self):
        return self.location_name


class Image(models.Model):
    name = models.CharField(max_length =30)
    image = models.ImageField(upload_to = 'image/')
    description = models.CharField(max_length =150)
    category = models.ForeignKey(Category, blank= True)
    location = models.ForeignKey(Location)
    capture_date = models.TimeField(auto_now_add=True) 

    def __str__(self):
      return self.name

    class Meta:
       ordering = ['name']

    def save_image(self):
      self.save()

    def delete_image(self):
      self.delete()

    def update_image(self):
      self.update()



    @classmethod
    def get_images(cls):
        all_images = Image.objects.all()
        return all_images

    @classmethod
    def get_image_by_id(self,id):
      image = Image.objects.get(id=id)
      return image


    @classmethod
    def search_image_category(cls,search_term):
      # category= Category.objects.get(category_name=search_term)
      images =cls.objects.filter(category__category_name__icontains =search_term)
      

      return images
    @classmethod
    def search_image_location(cls,search_term):
      # category= Category.objects.get(category_name=search_term)
      images =cls.objects.filter(location__location_name__icontains =search_term)
      

      return images



    @classmethod
    def filter_by_location(cls, filter_location):
        images_location = Image.objects.filter(location__id=filter_location)
        
        return images_location  

