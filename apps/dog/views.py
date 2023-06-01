from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from apps.dog.models import Dog
from apps.usermanagement.models import CustomUser
from apps.dog.forms import AddDogForm
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django.db.models import Q

@login_required(login_url='petpal_login')
def add_dog(request):
    try:
        valid_pet_owner = CustomUser.fetch_pet_owners.get(user_role='DUEÑO', id=request.user.id)
    except CustomUser.DoesNotExist or valid_pet_owner==None: 
        return redirect('home-page')
            
    if request.method == 'POST':
        form = AddDogForm(request.POST, request.FILES)
        if form.is_valid():
            #try:
            #    valid_pet_owner = CustomUser.fetch_pet_owners.get(user_role='DUEÑO', id=request.user.id)
            #except CustomUser.DoesNotExist or valid_pet_owner==None: 
            #    return redirect('home-page')
            if valid_pet_owner:
                pet_owner = form.save(commit=False)
                valid_dog_name = Dog.objects.filter(name=pet_owner.name, dog_owner_id=valid_pet_owner).first()
                if not valid_dog_name:
                    pet_owner.dog_owner_id = valid_pet_owner
                    pet_owner.save()
            return redirect('home-page')
    else:
        form=AddDogForm()
        
    return render(request,'dog/add_dog.html',
            {
            'form' : form,
            'error': form.errors
           
            }
    )      

@login_required(login_url='petpal_login')
def dogs_list(request):
    dogs = Dog.objects.filter(dog_owner_id=request.user.id)
    if not dogs:
        return redirect('add_dog')
        
    context = {"dogs": dogs}
    return render(request, 'dog/dogs_list.html', context )

@login_required(login_url='')
def destroy_dog(request,id):
    dog_to_destroy = Dog.objects.get(id=id)
    dog_to_destroy.delete()
    return redirect('dogs_list')
    
class DogUpdateView(UpdateView):
    model = Dog
    form_class = AddDogForm
    template_name = 'dog/dog_form.html'
    success_url = reverse_lazy('dogs_list')
    
    