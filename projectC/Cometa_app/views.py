from django.shortcuts import render


def home(request):
    return render(request, 'cometa/home/home.html')

