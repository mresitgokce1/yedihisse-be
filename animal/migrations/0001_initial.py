# Generated by Django 4.0.6 on 2022-07-12 22:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Değiştirilme Tarihi')),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktif Mi?')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Silindi Mi?')),
                ('age', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)], verbose_name='Hayvan Yaşı')),
                ('kilo', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Hayvan Kilosu')),
                ('code', models.CharField(max_length=255, unique=True, verbose_name='Hayvan Kodu')),
                ('cost', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50000)], verbose_name='Hayvan Maliyeti')),
                ('gain', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50000)], verbose_name='Hayvan Karı')),
                ('ear_code', models.CharField(blank=True, max_length=255, verbose_name='Hayvan Kulak Kodu')),
                ('bait_code', models.CharField(blank=True, max_length=255, verbose_name='Hayvan Yem Kodu')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimalType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Değiştirilme Tarihi')),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktif Mi?')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Silindi Mi?')),
                ('animal_type_name', models.CharField(max_length=50, unique=True, verbose_name='Hayvan Tip Adı')),
                ('can_allotment', models.BooleanField(default=False, verbose_name='Hayvan Hisse Edilebilir Mi?')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
