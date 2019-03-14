from django.db import models

class Image(models.Model):
    name = models.CharField(max_length =30)
    image = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    category = models.ForeignKey(Editor)
    Location = models.ForeignKey(Editor)
    capture_date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
       return self.name


class category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name



class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name