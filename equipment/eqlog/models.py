from datetime import date
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


class Equipment(models.Model):
    type = models.CharField(verbose_name='Тип оборудования', max_length=50)
    model = models.CharField(verbose_name='Модель', max_length=50)
    serial_number = models.CharField(verbose_name='Серийный номер', max_length=50)
    id_number = models.CharField(verbose_name='Инвентарный номер', max_length=10)
    sale_date = models.DateField(verbose_name='Дата покупки', default=date(2024, 1, 1))
    price = models.FloatField(verbose_name='Цена покупки', max_length=10)
    is_working = models.BooleanField(verbose_name='Работает', default=True)
    testing = models.BooleanField(verbose_name='Доступно для тестирования', default=False)
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    person = models.ForeignKey('Person', on_delete=models.PROTECT, verbose_name='Сотрудник', related_name='get_equipments')
    slug = models.SlugField(verbose_name='URL', max_length=255, unique=True, db_index=True)
    objects = models.Manager()

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('equipment', kwargs={'equip_slug': self.slug})

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'
        ordering = ['type', 'model']


class Person(models.Model):
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    middle_name = models.CharField(verbose_name='Отчество', max_length=50)
    department = models.ForeignKey('Department', on_delete=models.PROTECT, verbose_name='Отдел', related_name='get_persons')
    job_title = models.CharField(verbose_name='Должность', max_length=50)
    jobing_at = models.DateField(verbose_name='Дата трудоустройства', default=date(2020, 1, 1))
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    remote = models.BooleanField(verbose_name='Удаленщик', default=False)
    is_working = models.BooleanField(verbose_name='Работает', default=True)
    city = models.CharField(verbose_name='Город', max_length=50, default='Москва')
    slug = models.SlugField(verbose_name='URL', max_length=255, unique=True, db_index=True)
    objects = models.Manager()

    @property
    def fio(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    def get_absolute_url(self):
        return reverse('person', kwargs={'pers_slug': self.slug})

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return self.fio

class Department(models.Model):
    name = models.CharField(verbose_name='Отдел', max_length=50)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'