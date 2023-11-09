from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'titan/home/home.html')

def publications(request):
    return render(request, 'titan/home/publications.html')