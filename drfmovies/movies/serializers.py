import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Movies


class MoviesModel:
    def __init__(self, title, plot):
        self.title = title
        self.plot = plot


class MoviesSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    plot = serializers.CharField()


def encode():
    """
    простая функция наглядно показывающая преобразование
    объекта в json
    """
    # создаем объект модели
    model = MoviesModel('Predator', 'Predator fucked up from Arnie')
    # создаем объект сериализатора, который создает
    # спец.коллекцию data, состоящую из значений объекта
    model_sr = MoviesSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    # словарь преобразовываем в json строку
    json = JSONRenderer().render(model_sr.data)
    print(json)


def decode():
    """
    обратная функция наглядно показывающая преобразование
    объекта из json в словарь
    """
    stream = io.BytesIO(b'{"title":"Predator","plot":"Predator fucked up from Arnie"}')
    data = JSONParser().parse(stream)
    serializer = MoviesSerializer(data=data)
    serializer.is_valid()

    print(serializer.validated_data)
    # Вывод OrderedDict([('title', 'Predator'),
    # ('plot', 'Predator fucked up from Arnie')])







