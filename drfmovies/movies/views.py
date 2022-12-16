from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Movies, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import MoviesSerializer


class MoviesAPIList(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class MoviesAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    # удалять может только автор записи
    permission_classes = (IsOwnerOrReadOnly,)


class MoviesAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    permission_classes = (IsAdminOrReadOnly,)







# убран, чтобы нагляднее посмотреть работу permissions
# class MoviesViewSet(viewsets.ModelViewSet):
#     # queryset = Movies.objects.all()
#     serializer_class = MoviesSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#         if not pk:
#             return Movies.objects.all()[:3]
#
#         return Movies.objects.filter(pk=pk)
#
#     # декоратор, добавляющий нестандартный маршрут
#     # отображение конкретной категории
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': [cats.title_cat]})


    # отображение всех категорий
    # @action(methods=['get'], detail=False)
    # def category(self, request):
    #     cats = Category.objects.all()
    #     return Response({'cats': [c.title_cat for c in cats]})






# класс одновременно представляет список объектов, а также создает объект
# class MoviesAPIList(generics.ListCreateAPIView):
#     queryset = Movies.objects.all()
#     serializer_class = MoviesSerializer


# class MoviesAPIUpdate(generics.UpdateAPIView):
#     queryset = Movies.objects.all()
#     serializer_class = MoviesSerializer


# class MoviesAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movies.objects.all()
#     serializer_class = MoviesSerializer


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











