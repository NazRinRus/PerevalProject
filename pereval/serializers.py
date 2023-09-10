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

# Сериализер таблицы содержащей ссылки на оббъект таблицы Перевал и Фотографии
class PerevalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = ('pereval', 'images')

class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height')

class PerevalAddedSerializer(serializers.ModelSerializer):
    user = UsersSerializer(required=False)
    coord_id = CoordsSerializer(required=False)
    images = ImagesSerializer()#many=True
    class Meta:
        model = PerevalAdded
        fields = ('status', 'beautyTitle', 'title', 'other_titles', 'connect', 'add_time', 'coord_id',
                  'winter', 'summer', 'autumn', 'spring', 'user', 'images')

    def create(self, validated_data):
        # разбиваем словарь validated_data на таблицы
        user = validated_data.pop('user')
        coords = validated_data.pop('coord_id')
        images = validated_data.pop('images')
        # Создаем нового автора или возвращаем модель существующего
        current_user = Users.objects.filter(mail=user['mail'])
        if current_user.exists():
            user_serializers = UsersSerializer(data=user)
            user_serializers.is_valid(raise_exception=True)
            user = user_serializers.save()
        else:
            user = Users.objects.create(**user)

        coords = Coords.objects.create(**coords)

        pereval_new = PerevalAdded.objects.create(**validated_data, images=images, author=user, coord_id=coords)

        if images:
            for imag in images:
                name = imag.pop('name')
                photos = photos.pop('photos')
                img_new = Images.objects.create(name=name, photos=photos)
                PerevalImages.objects.create(pereval=pereval_new, images=img_new)

        return pereval_new

    def validate(self, data):
        if self.instance is not None:
            instance_user = self.instance.user
            data_user = data.get('user')
            user_fields_for_validation = [
                instance_user.surname != data_user['surname'],
                instance_user.name != data_user['name'],
                instance_user.otch != data_user['otch'],
                instance_user.phone != data_user['phone'],
                instance_user.mail != data_user['mail'],
            ]
            if data_user is not None and any(user_fields_for_validation):
                raise serializers.ValidationError(
                    {
                        'Отказано': 'Данные пользователя не могут быть изменены',
                    }
                )
        return data

