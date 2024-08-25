from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings

app_name = 'exoplanets_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('listar_objetos/', views.listar_objetos, name='listar_objetos'),
    path('metodos_detec/', views.detection_methods, name='detection_methods'),
    path('lightcurve_analysis/', views.lightcurve_analysis, name='lightcurve_analysis'),
]
