from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings

app_name = 'Capp'

urlpatterns = [
    path('catalog_home/', views.home,  name='home'),
    path('page/<int:kic>/', views.pagina_objetos, name='pagina_objetos'),
    
]
