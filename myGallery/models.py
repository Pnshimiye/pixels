from django.db import models
import datetime as dt




class Category(models.Model):
    category_name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Location(models.Model):
    location_name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length =30)
    image = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    category = models.ForeignKey(Category)
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

    def get_image_by_id(self,id):
      image = Image.objects.get(id=id)
      return image

    def search_image_category(self,this_category):
        category_image =Image.objects.filter_by(category_name=this_category)
        return category_image

    def searc_image_by_location(self,this_location):
        location_image= Image.objects.filter_by(location_name=this_location)
        return location_image
  


