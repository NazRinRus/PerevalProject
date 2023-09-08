from rest_framework import serializers
from .models import *



class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('mail', 'phone', 'name', 'surname', 'otch')

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('name', 'photos', 'pereval')

class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height')

class PerevalAddedSerializer(serializers.ModelSerializer):
    user1 = UsersSerializer()
    coords = CoordsSerializer()
    images = ImagesSerializer(many=True)
    class Meta:
        model = PerevalAdded
        fields = ('status', 'beautyTitle', 'title', 'other_titles', 'connect', 'add_time', 'coord_id',
                  'winter_lvl', 'summer_lvl', 'autumn_lvl', 'spring_lvl', 'author', 'images')

    def create(self, validated_data):
        # разбиваем словарь validated_data на таблицы
        user = validated_data.pop('user')
        coords = validated_data.pop('coords')
        images = validated_data.pop('images')
        # Создаем нового автора или возвращаем модель существующего
        current_user = Users.objects.filter(mail=user['email'])
        if current_user.exists():
            user_serializers = UsersSerializer(data=user)
            user_serializers.is_valid(raise_exception=True)
            user = user_serializers.save()
        else:
            user = Users.objects.create(**user)
        coords = Coords.objects.create(**coords)
        perevall = PerevalAdded.objects.create(**validated_data, images=images, author=user,
                                               coords=coords)

        if images:
            for imag in images:
                name = imag.pop(name)
                photos = photos.pop(photos)
                Images.objects.create(perevall=perevall, name=name, photo=photos)
        return perevall

