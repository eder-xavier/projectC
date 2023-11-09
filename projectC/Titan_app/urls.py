from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'Titan_app'

urlpatterns = [
    path('', views.home,  name='home'),
    path('extencoes/', views.publications,  name='publications'),
]
