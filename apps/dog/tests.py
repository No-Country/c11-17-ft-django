from django.test import TestCase
from apps.dog.models import Dog


class StateTestCase(TestCase):
 
    def setUp(self):
        print("Setting up test Dog case")

    def tearDown(self): 
        print("Ending test Dog case")
        
    def test_total_records(self):
        Dog.objects.create(dog_owner_id="1",
                           name="rene", breed="Chihuhua",
                           photo="/media/image1.png")
        record_set = Dog.objects.all()
        self.assertEqual(1,record_set)
        
      