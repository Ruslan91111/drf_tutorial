from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movies
from .serializers import MoviesSerializer


class MoviesAPIView(APIView):
    def get(self, request):
        list_of_movies = Movies.objects.all().values()
        return Response({'movies': list(list_of_movies)})

    def post(self, request):
        movie_new = Movies.objects.create(
            title=request.data['title'],
            plot=request.data['plot'],
            cat_id=request.data['cat_id']
        )

        return Response({'movie': model_to_dict(movie_new)})





