from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

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

# Create your views here.
