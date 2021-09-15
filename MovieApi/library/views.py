from rest_framework import generics, permissions
from .models import Genere,Movie
from .serializers import GenereSerilizer, MovieSerilizer

# Create your views here.

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = MovieSerilizer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = MovieSerilizer