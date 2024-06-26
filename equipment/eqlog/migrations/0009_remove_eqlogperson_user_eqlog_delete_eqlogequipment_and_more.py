# Generated by Django 5.0.2 on 2024-05-03 06:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eqlog', '0008_eqlogequipment_equipment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eqlogperson',
            name='user',
        ),
        migrations.CreateModel(
            name='Eqlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.TextField(verbose_name='Имя модели')),
                ('attr_name', models.TextField(verbose_name='Изменяемое поле')),
                ('old_value', models.TextField(verbose_name='Старое значение')),
                ('new_value', models.TextField(verbose_name='Новое значение')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.DeleteModel(
            name='EqlogEquipment',
        ),
        migrations.DeleteModel(
            name='EqlogPerson',
        ),
    ]
