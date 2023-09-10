# Виртуальная стажировка. Проект Pereval

# 1. Создание виртуального окружения:
python3 -m venv venv_pereval
# 2. Активировать виртуальное окружение:
source venv_pereval/bin/activate
# 3. Установка django:
pip3 install django
# 4. Создание проекта PerevalProject:
django-admin startproject PervalProject
# 5. Создание приложения pereval:
cd PerevalProject
python3 manage.py startapp pereval
# 6. Создание базы данных postgresql в терминале:
**Используемая СУБД - PostgreSQL**

Командная строка postgresql:
**sudo -i -u postgres**

Создать БД:
**createdb pereval_db**

Консоль суперпользователя:
**psql**

Установить пароль суперпользователя:
**ALTER USER postgres WITH PASSWORD 'мой стандартный пароль';**

Создать нового пользователя:
**CREATE USER nazrinrus WITH PASSWORD 'мой стандартный пароль';**

Дал права суперпользователя новому пользователю:
**ALTER USER nazrinrus WITH SUPERUSER;**

Команды: 
**\q** выход с консоли суперюзера;
**\l** просмотр существующих БД;
**\du** просмотр списка пользователей;
**exit** выход с консоли postgresql/

# 7. Описание моделей:

Данные, являющиеся константами, практически не изменяющиеся, выведены за пределы моделей в списки кортежей, такие как:

1) Активность - способ прохождения локации, вывел в список кортежей

`ACTIVITIES = [
    ('foot', 'пеший'),
    ('bike', 'велосипед'),
    ('car', 'автомобиль'),
    ('motorbike', 'мотоцикл'),
]`

2) Вид локации, вывел в список кортежей

`BEAUTYTITLE = [
    ('poss', 'перевал'),
    ('mountain_peak', 'горная вершина'),
    ('gorge', 'ущелье'),
    ('plateau', 'плато'),
]`

3) статус добавленной записи пользователя, списком кортежей
`STATUS = [
    ('new', 'новый'),
    ('pending', 'на модерации'),
    ('accepted', 'принят'),
    ('rejected', 'не принят'),
]`

4) Уровень сложности прохождения локации, списком кортежей
`LEVELS = [
    ('', 'не указано'),
    ('1A', '1a'),
    ('1B', '1б'),
    ('2А', '2а'),
    ('2В', '2б'),
    ('3А', '3а'),
    ('3В', '3б'),
    ]`

*Модель PerevalAdded - основные данные добавленные туристом:*

`class PerevalAdded(models.Model):
    status = models.CharField(choices=STATUS, max_length=25, default='new') #статус нового сообщения, по умолчанию Новое
    beautyTitle = models.CharField('тип', choices=BEAUTYTITLE, max_length=50)#тип локации - перевал, ущелье и т.д. списком
    title = models.CharField('название', max_length=50, blank=True)# название локации
    other_titles = models.CharField('иные названия', max_length=50)# описание локации
    connect = models.CharField('соединение', max_length=250)# какие локации соединяет (применимо к перевалу)
    add_time = models.DateTimeField(default=timezone.now, editable=False)#дата/время создания записи (не понял пользователь вручную создает или автоматическое поле при добавлении в БД)
    coord_id = models.OneToOneField(Coords, on_delete=models.CASCADE)# ссылка на объект с координатами локации. Зачем если связь один к одному?
    winter = models.CharField('зима', max_length=2, choices=LEVELS)# уровень сложности прохождения локации зимой
    summer = models.CharField('лето', max_length=2, choices=LEVELS)# уровень сложности прохождения локации летом
    autumn = models.CharField('осень', max_length=2, choices=LEVELS)# уровень сложности прохождения локации осенью
    spring = models.CharField('весна', max_length=2, choices=LEVELS)# уровень сложности прохождения локации весной
    author = models.ForeignKey(Users, on_delete=models.CASCADE)# автор статьи - ссылка на объект пользователей`

*Модель User - основные данные о туристе:*

`class Users(models.Model):
    mail = models.EmailField('почта', unique=True)# поле электронной почты, оно уникально, по нему проверяю ункикальность пользователей
    phone = models.CharField('телефон', max_length=15)
    name = models.CharField('имя', max_length=30)
    surname = models.CharField('фамилия', max_length=30)
    otch = models.CharField('отчество', max_length=30)

    def __str__(self):
        return f'{self.surname}'`

*Модель Coords - Координаты локации, переданные туристом*

`class Coords(models.Model):
    latitude = models.FloatField('широта', max_length=9, blank=True)
    longitude = models.FloatField('долгота', max_length=9, blank=True)
    height = models.IntegerField('высота', blank=True)`

*класс Images фотографии добавленные пользователем*

`class Images(models.Model):
    name = models.CharField(max_length=50)# название фотографии
    photos = models.ImageField('Фото', upload_to=get_image_path, blank=True, null=True)# объект фотографии`

*Класс PerevalImages таблица объединяющая объекты таблиц PerevalAdded и Images*

`class PerevalImages(models.Model):
    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE, default=0)  # ссылка на объект локации
    images = models.ForeignKey(Images, on_delete=models.CASCADE, default=0)  # ссылка на объект фотографии`

# 8 Проектирование Views и Serializers

*установка Django Rest Framework:*
`pip install djangorestframework`

Для заполнения и тестирования работоспособности отдельных таблиц, создал 
классы для отдельных таблиц на основе generics.ListCreateAPIView и generics.RetrieveUpdateDestroyAPIView, 
доступные по запросу api/v1/название_модели - для просмотра списком или добавления, 
api/v1/название_модели/pk - для редактирования, удаления.

Для реализации метода submitData используются классы на основе viewsets.ModelViewSet,
доступные по запросу api/v2/название_модели

Реализация метода submitData заключается в том, что турист (клиентское приложение)
отправляет POST запрос в формате JSON содержащий все необходимые данные.
Далее, полученный от туриста JSON на стадии валидации переводится в список словарей validated_data
который разделяется на блоки, содержащие данные отдельных талиц,
например Users, Coords, Images

`user = validated_data.pop('user')
coords = validated_data.pop('coord_id')
images = validated_data.pop('images')`

Отдельные блоки данных сохраняются в побочные таблицы:

`user = Users.objects.create(**user)
coords = Coords.objects.create(**coords)`

затем в основную таблицу PerevalAdded добаляются оставшиеся данные и ссылки на побочные объекты таблиц

`pereval_new = PerevalAdded.objects.create(**validated_data, images=images, author=user, coord_id=coords)`


