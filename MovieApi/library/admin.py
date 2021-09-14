from django.contrib import admin
from django.db.models.base import Model
from .models import Genere, Movie

# Register your models here.

admin.site.register(Genere)
admin.site.register(Movie)