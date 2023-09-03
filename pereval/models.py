from django.db import models
from django.utils import timezone



ACTIVITIES = [
    ('foot', 'пеший'),
    ('bike', 'велосипед'),
    ('car', 'автомобиль'),
    ('motorbike', 'мотоцикл'),
]

BEAUTYTITLE = [
    ('poss', 'перевал'),
    ('mountain_peak', 'горная вершина'),
    ('gorge', 'ущелье'),
    ('plateau', 'плато'),
]


STATUS = [
    ('new', 'новый'),
    ('pending', 'на модерации'),
    ('accepted', 'принят'),
    ('rejected', 'не принят'),
]

LEVELS = [
    ('', 'не указано'),
    ('1A', '1a'),
    ('1B', '1б'),
    ('2А', '2а'),
    ('2В', '2б'),
    ('3А', '3а'),
    ('3В', '3б'),
    ]


class Users(models.Model):

    mail = models.EmailField('почта', unique=True)
    phone = models.IntegerField('телефон', max_length=12)
    name = models.CharField('имя', max_length=30)
    surname = models.CharField('фамилия', max_length=30)
    otch = models.CharField('отчество', max_length=30)

    def __str__(self):
        return f'{self.surname}'


class Coords(models.Model):

    latitude = models.FloatField('широта', max_length=9, blank=True)
    longitude = models.FloatField('долгота', max_length=9, blank=True)
    height = models.IntegerField('высота', max_length=5, blank=True)


class Images(models.Model):
    name = models.CharField(max_length=50)
    photos = models.ImageField('Фото', upload_to=get_image_path, blank=True, null=True)


class PerevalAdded(models.Model):

    status = models.CharField(choices=STATUS, max_length=25, default='new')
    beautyTitle = models.CharField('тип', choices=BEAUTYTITLE, max_length=50)
    title = models.CharField('название', max_length=50, blank=True)
    other_titles = models.CharField('иные названия', max_length=50)
    connect = models.CharField('соединение', max_length=250)
    add_time = models.DateTimeField(default=timezone.now, editable=False)
    images = models.ForeignKey(Images, on_delete=models.CASCADE, default=0)
    coord_id = models.OneToOneField(Coords, on_delete=models.CASCADE)
    winter_lvl = models.CharField('зима', max_length=2, choices=LEVELS)
    summer_lvl = models.CharField('лето', max_length=2, choices=LEVELS)
    autumn_lvl = models.CharField('осень', max_length=2, choices=LEVELS)
    spring_lvl = models.CharField('весна', max_length=2, choices=LEVELS)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)


class PerevalAreas(models.Model):

    id_parent = models.IntegerField(max_length=8, blank=True)
    title = models.TextField()


class PerevalImages(models.Model):
    id_pereval = models.ForeignKey(PerevalAreas, on_delete=models.CASCADE, default=0)
    id_images = models.ForeignKey(Images, on_delete=models.CASCADE, default=0)