# Generated by Django 5.0.2 on 2024-04-10 05:55

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Отдел')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.CreateModel(
            name='SettingID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(default='ГM-', max_length=10, verbose_name='Префикс инвентарного номера')),
                ('id_l', models.IntegerField(default='6', verbose_name='Длина цифровой части инв.номера')),
            ],
            options={
                'verbose_name': 'Настройки инв.номера',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=50, verbose_name='Отчество')),
                ('job_title', models.CharField(max_length=50, verbose_name='Должность')),
                ('jobing_at', models.DateField(default=datetime.date(2024, 1, 1), verbose_name='Дата трудоустройства')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('remote', models.BooleanField(default=False, verbose_name='Удаленщик')),
                ('is_working', models.BooleanField(default=True, verbose_name='Работает')),
                ('city', models.CharField(default='Москва', max_length=50, verbose_name='Город')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_persons', to='eqlog.department', verbose_name='Отдел')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Тип оборудования')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('serial_number', models.CharField(max_length=50, verbose_name='Серийный номер')),
                ('id_number', models.CharField(max_length=10, unique=True, verbose_name='Инвентарный номер')),
                ('sale_date', models.DateField(default=datetime.date(2024, 1, 1), verbose_name='Дата покупки')),
                ('price', models.FloatField(max_length=10, verbose_name='Цена покупки')),
                ('is_working', models.BooleanField(default=True, verbose_name='Работает')),
                ('testing', models.BooleanField(default=False, verbose_name='Доступно для тестирования')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_equipments', to='eqlog.person', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Оборудование',
                'ordering': ['type', 'model'],
            },
        ),
    ]
