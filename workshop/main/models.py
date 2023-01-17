from django.db import models

from users.models import CustomUser


class Status(models.TextChoices):
    """Статусы заявки"""
    CREATED = 'CREATED', 'Новая заявка'
    CONFIRMED = 'CONFIRMED', 'Подтверждена менеджером'
    READY_TO_WORK = 'READY_TO_WORK', 'Готова к работе'
    PROGRESS = 'PROGRESS', 'Выполняется'
    VERIFICATION = 'VERIFICATION', 'Ремонт выполнен'
    TESTS = 'TESTS', 'На проверку'
    RE_REPAIR = 'RE_REPAIR', 'На доработку'


class PlacesToWork(models.Model):
    """Место ремонта"""
    name = models.CharField(max_length=100, verbose_name='Место ремонта')

    class Meta:
        verbose_name = 'Место ремонта'
        verbose_name_plural = 'Места ремонта'

    def __str__(self):
        return self.name


class TypeRepair(models.Model):
    """Тип ремонта"""
    name = models.CharField(max_length=255, verbose_name='Тип ремонта')
    hours = models.PositiveSmallIntegerField(verbose_name='Часов для ремонта')

    class Meta:
        verbose_name = 'Тип работы'
        verbose_name_plural = 'Типы работ'

    def __str__(self):
        return self.name


class Works(models.Model):
    """Работы"""
    name = models.CharField(max_length=255, verbose_name='Тип работы')

    class Meta:
        verbose_name = 'Тип работы'
        verbose_name_plural = 'Типы работ'

    def __str__(self):
        return self.name


class Parts(models.Model):
    """Запчасти"""
    name = models.CharField(max_length=255, verbose_name='Тип детали', null=True, blank=True)
    brand = models.CharField(max_length=255, default='', verbose_name='Бренд детали')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Цена детали')
    count_parts = models.IntegerField(default=0, verbose_name='Количество деталей')

    class Meta:
        verbose_name = 'Тип детали'
        verbose_name_plural = 'Типы деталей'

    def __str__(self):
        return f'{self.name}\n{self.brand}\nОсталось: {self.count_parts} шт.'
        

class CarBrand(models.Model):
    """Бренд автомобиля"""
    brand = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Бренд автомобиля'
        verbose_name_plural = 'Бренд автомобиля'

    def __str__(self):
        return self.brand


class Application(models.Model):
    """Новая заявка"""
    users = models.ManyToManyField(CustomUser, verbose_name='Участники заявки')
    description = models.TextField(verbose_name='Описание поломки')
    status = models.CharField('Статус', max_length=50, choices=Status.choices, default=Status.CREATED)
    time_to_work = models.DateTimeField(verbose_name='Время принятия в работу', null=True, blank=True)
    completion_time = models.DateTimeField(verbose_name='Время завершения ремонта', null=True, blank=False)
    places_to_work = models.ForeignKey(PlacesToWork, related_name='place_to_application', on_delete=models.PROTECT,
                                       verbose_name='Место ремонта', null=True, blank=True)
    type_repair = models.ForeignKey(TypeRepair, related_name='type_repairs', on_delete=models.PROTECT,
                                    null=True, blank=True)
    works = models.ManyToManyField(Works, verbose_name='Работы', related_name='work_repairs')
    parts = models.ManyToManyField(Parts, verbose_name='Запчасти', related_name='part_repairs')
    car = models.ForeignKey(CarBrand, related_name='car_repairs', on_delete=models.PROTECT, verbose_name='Автомобиль',
                            null=True, blank=True)
    car_vin = models.CharField(max_length=17, null=True)
    year = models.CharField(max_length=30, null=True)
    state_number = models.CharField(max_length=15, null=True)
    name_client = models.CharField(max_length=30, null=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'ТЗ№ {self.pk}'

    def get_absolute_url(self):
        return f'/main/{self.pk}'
