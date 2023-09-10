from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from  rest_framework import viewsets

# сериализеры для работы с данными таблиц, просмотр, добавление, удаление
class PerevalAddedListAPIView(generics.ListCreateAPIView):# сериализер для работы с таблицей перевалов, просмотр, добавление
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer

class PerevalAddedDetailAPIView(generics.RetrieveUpdateDestroyAPIView):# универсальный сериализер для работы с объектом перевалов, редактирование, удаление
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer

class UsersListAPIView(generics.ListCreateAPIView):# универсальный сериализер для работы с таблицей пользователей, просмотр, добавление
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):# универсальный сериализер для работы с объектом пользователей, редактирование, удаление
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class ImagesListAPIView(generics.ListCreateAPIView):# сериализер для работы с таблицей фотографий, просмотр, добавление
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

class ImagesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):# универсальный сериализер для работы с объектом фотографии, редактирование, удаление
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

class CoordsListAPIView(generics.ListCreateAPIView):# сериализер для работы с таблицей координат, просмотр, добавление
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer

class CoordsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):# универсальный сериализер для работы с объектом координат, редактирование, удаление
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer

# Классы для реализации submitData, так же универсальные, можно добавлять, редактировать, удалять, просматривать, доступны по адресу api/v2/
class PerevalAddedViewSet(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

class PervalImagesViewSet(viewsets.ModelViewSet):
    queryset = PerevalImages.objects.all()
    serializer_class = PerevalImagesSerializer

class CoordViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


