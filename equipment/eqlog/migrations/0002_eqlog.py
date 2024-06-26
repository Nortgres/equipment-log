# Generated by Django 5.0.2 on 2024-04-20 16:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eqlog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Eqlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_value', models.TextField(verbose_name='Старое значение')),
                ('new_value', models.TextField(verbose_name='Новое значение')),
                ('id_number', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_id_number', to='eqlog.equipment', verbose_name='Инвентарный номер')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
