# Generated by Django 5.0.2 on 2024-04-20 18:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eqlog', '0005_alter_equipment_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eqlog',
            name='id_number',
        ),
        migrations.AddField(
            model_name='eqlog',
            name='field_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eqlog',
            name='id_equipments',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eqlog',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
