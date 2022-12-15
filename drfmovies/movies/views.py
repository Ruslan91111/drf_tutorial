from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movies
from .serializers import MoviesSerializer


class MoviesAPIView(APIView):
    def get(self, request):
        list_of_movies = Movies.objects.all()
        # список передаем на сериализатор, устанавливаем параметр many=True,
        # чтобы обрабатывало список, а не одну запись
        # затем преобразовывает в байтовую json строку
        # по сути data ниже выполняет все те же функии, что и encode()
        return Response({'movies': MoviesSerializer(list_of_movies, many=True).data})

    def post(self, request):
        # проверка валидности передаваемых данных
        serializer = MoviesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        movie_new = Movies.objects.create(
            title=request.data['title'],
            plot=request.data['plot'],
            cat_id=request.data['cat_id']
        )

        return Response({'movie': MoviesSerializer(movie_new).data})





