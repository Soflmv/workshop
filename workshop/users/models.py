from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .manager import CustomUserManager


class Role(models.TextChoices):
    """Роли пользователей"""
    CUSTOMER = 'CUSTOMER', 'Клиент'
    MANAGER = 'MANAGER', 'Менеджер'
    MASTER = 'MASTER', 'Мастер'
    WORKER = 'WORKER', 'Механик'


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Модель пользователя при регистрации"""
    role = models.CharField('Роль пользователя', max_length=20,
                            choices=Role.choices,
                            default=Role.CUSTOMER)
    email = models.EmailField(_('* Email'), unique=True)
    first_name = models.CharField('* Имя', max_length=100, null=True, default='')
    last_name = models.CharField('* Фамилия', max_length=100, null=True, default='')
    phone = models.CharField('* Телефон', max_length=25, default='')
    is_staff = models.BooleanField('Суперпользователь', default=False)
    is_active = models.BooleanField('Активен', default=True)
    date_joined = models.DateTimeField('Дата последнего входа', default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'






























