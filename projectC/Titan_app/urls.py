from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'Titan_app'

urlpatterns = [
    path('', views.home,  name='home'),
    path('publicacoes/', views.publications,  name='publications'),
    path('extensoes/', views.extensions,  name='extensions'),
    #path('noticias/', views.public_news, name='news'),
#
    #path('signup/', views.signup, name='signup'),
    #path('login/', views.user_login, name='login'),
    #path('registration_code/', views.registration_code, name='registration_code'),
#
    #path('profile/<str:username>/', views.view_profile, name='view_profile'),
    #path('edit_profile/', views.edit_profile, name='edit_profile'),
    #path('logout/', views.user_logout, name='user_logout'),
#
    #path('user/news/create/', views.create_news, name='create_news'),
    #path('user/news/edit/<int:news_id>/', views.edit_news, name='edit_news'),
    #path('user/news/delete/<int:news_id>/', views.delete_news, name='delete_news'),
    

]

