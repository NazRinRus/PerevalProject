from rest_framework import serializers
from .models import *

class PerevalAddedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = ('status', 'beautyTitle', 'title', 'other_titles', 'connect', 'add_time', 'images', 'coord_id',
                  'winter_lvl', 'summer_lvl', 'autumn_lvl', 'spring_lvl', 'author')

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('mail', 'phone', 'name', 'surname', 'otch')

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('name', 'photos')

class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height')

