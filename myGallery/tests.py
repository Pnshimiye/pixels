from django.test import TestCase
from .models import Location, Category, Image 
 

 
class LocationTestClass(TestCase):
    # Set Up Method
    def setUp(self):
        self.kigali = Location(location_name='kigali')
        self.kigali.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.kigali,Location))
    
    def test_updating_location(self):
        location = Location.get_location_id(self.kigali.id)
        location.update_location('upcountry')
        location = Location.get_location_id(self.kigali.id)
        self.assertTrue(location.location_name == 'upcountry')
    
    def tearDown(self):
        self.kigali.delete_location()
    
class CategoryTestClass(TestCase):
    # Set Up Method
    def setUp(self):
        self.food = Category(photo_category='Food')
        self.food.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category))
    
    def tearDown(self):
        self.food.delete_category()
    
    def test_updating_category(self):
        category = Category.get_category_id(self.food.id)
        category.update_category('people')
        category = Category.get_category_id(self.food.id)
        self.assertTrue(category.category_name == 'people')
    
class ImageTestCase(TestCase):
    # Set Up Method
    def setUp(self):
        self.food = Category(category_name='Food')
        self.food.save_category()

        self.nairobi = Location(location_name='Kigali')
        self.nairobi.save_location()

        self.image = Image(name='Sea food',description="Sea food form Sakae a Japanese restaurant", location = self.location, category= self.category)
        self.image.save_image()
    
    def tearDown(self):
        self.image.delete_image()
        self.food.delete_category()
        self.kigali.delete_location()
    
    def test_get_images(self):
        images = Image.get_images()
        self.assertTrue(len(images)>0)
    
    def test_get_image_by_id(self):
        images = Image.get_image_by_id(self.image.id)
        self.assertTrue(images == self.image)

    def test_search_image(self):
        images = Image.search_image('Food')
        self.assertTrue(len(images)>0)
    
    def test_filter_by_location(self):
        images = Image.filter_by_location('Kigali')
        self.assertTrue(len(images)>0)