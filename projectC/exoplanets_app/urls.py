from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings

app_name = 'exoplanets_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('listar_objetos/', views.listar_objetos, name='listar_objetos'),
     path('workspace/', views.exoplanet_discovery, name='exoplanet_discovery'),
    path('generate_lightcurve/', views.generate_lightcurve, name='generate_lightcurve'),
    path('estimate_period/', views.estimate_period, name='estimate_period'),
    path('identify_exoplanet/', views.identify_exoplanet, name='identify_exoplanet'),
]
