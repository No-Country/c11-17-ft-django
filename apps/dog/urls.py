from django.urls import path

from apps.dog.views import add_dog, dogs_list, destroy_dog
urlpatterns = [
    path('add-dog/',add_dog,name='add-dog'),
    path('dogs-list/',dogs_list,name='dogs-list'),
    path('destroy-dog/<int:id>',destroy_dog,name='destroy-dog'),
]