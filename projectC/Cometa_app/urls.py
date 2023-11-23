from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'Cometa_app'

urlpatterns = [
    path('home/', views.home,  name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('home_admin/', views.home_admin, name='home_admin'),
    path('registration_code/', views.registration_code, name='registration_code'),
]
