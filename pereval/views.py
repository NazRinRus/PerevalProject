from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from  rest_framework import viewsets

class PerevalAddedListAPIView(generics.ListCreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer

class PerevalAddedDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer

class UsersListAPIView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class ImagesListAPIView(generics.ListCreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

class ImagesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

class CoordsListAPIView(generics.ListCreateAPIView):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer

class CoordsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer

# Классы для реализации submitData
class PerevalAddedViewSet(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

class CoordViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


