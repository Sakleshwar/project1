from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "index.html")

def aboutus(request):
    return render(request, "about.html")

def Registration(request):
    return render(request, "RegistrationForm.html")