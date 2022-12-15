import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.serializers import ModelSerializer

from .models import Movies


# class MoviesModel:
#     def __init__(self, title, plot):
#         self.title = title
#         self.plot = plot


class MoviesSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    plot = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Movies.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.plot = validated_data.get("plot", instance.plot)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance







# def encode():
#     """
#     простая функция наглядно показывающая преобразование
#     объекта в json
#     """
#     # создаем объект модели
#     model = MoviesModel('Predator', 'Predator fucked up from Arnie')
#     # создаем объект сериализатора, который создает
#     # спец.коллекцию data, состоящую из значений объекта
#     model_sr = MoviesSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     # словарь преобразовываем в json строку
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     """
#     обратная функция наглядно показывающая преобразование
#     объекта из json в словарь
#     """
#     stream = io.BytesIO(b'{"title":"Predator","plot":"Predator fucked up from Arnie"}')
#     data = JSONParser().parse(stream)
#     serializer = MoviesSerializer(data=data)
#     serializer.is_valid()
#
#     print(serializer.validated_data)
    # Вывод OrderedDict([('title', 'Predator'),
    # ('plot', 'Predator fucked up from Arnie')])







