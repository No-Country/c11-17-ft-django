from django.urls import path

from apps.dog.views import add_dog, \
      dogs_list, destroy_dog, DogUpdateView
urlpatterns = [
    path('add-dog/',add_dog,name='add-dog'),
    path('dogs-list/',dogs_list,name='dogs-list'),
    path('destroy-dog/<int:id>',destroy_dog,name='destroy-dog'),
    path('<int:pk>/edit/', DogUpdateView.as_view(), name='dog_edit'),
]