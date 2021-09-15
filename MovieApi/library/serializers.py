from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Movie,Genere

class GenereSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Genere
        fields = ['name','description']

class MovieSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['pk','title','release_date','genere','director','rating','description']

        extra_kwargs = {
            "description":{"required":False}
        }

        