from django.shortcuts import render

def home_page(request):
    context = {"welcome": "Welcome to PetPal"}
    return render(request,"homepage/index.html",context)    