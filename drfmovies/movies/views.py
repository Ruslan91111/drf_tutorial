from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movies
from .serializers import MoviesSerializer


# класс одновременно представляет список объектов, а также создает объект
class MoviesAPIList(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer


class MoviesAPIUpdate(generics.UpdateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer


class MoviesAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer




# class MoviesAPIView(APIView):
#     def get(self, request):
#         list_of_movies = Movies.objects.all()
#         # список передаем на сериализатор, устанавливаем параметр many=True,
#         # чтобы обрабатывало список, а не одну запись
#         # затем преобразовывает в байтовую json строку
#         # по сути data ниже выполняет все те же функии, что и encode()
#         return Response({'movies': MoviesSerializer(list_of_movies, many=True).data})
#
#     def post(self, request):
#         # проверка валидности передаваемых данных
#         serializer = MoviesSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'movie': serializer.data})
#
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Movies.objects.get(pk=pk)
#         except:
#             return Response({"error": "Objects does not exists"})
#
#         serializer = MoviesSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"movie": serializer.data})











