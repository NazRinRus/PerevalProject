from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

class PerevalAddedListAPIView(generics.ListCreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer

# Create your views here.
