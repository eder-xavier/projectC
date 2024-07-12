from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import OutVariation, WithVariation

admin.site.register(OutVariation)
admin.site.register(WithVariation)