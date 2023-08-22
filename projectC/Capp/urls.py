from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    #path('endereço/', MinhaView.as_view(), name='nome-da-url')
    path('', views.home,  name='home'),
    path('article/', views.article,  name='article'),
    path('pagina/<int:kic>/', views.pagina_objetos, name='pagina_objetos'),
    #path('figskic3228863/', views.figskic3228863, name='figskic3228863'),
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)