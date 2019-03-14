from django.db import models
import datetime as dt




class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
class Image(models.Model):
    name = models.CharField(max_length =30)
    image = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)
    capture_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.name

    class Meta:
      ordering = ['name']


