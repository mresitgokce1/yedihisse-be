# Generated by Django 4.0.6 on 2022-07-12 22:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car', '0003_alter_car_cattle_capacity_alter_car_ovine_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarManagerMission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Değiştirilme Tarihi')),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktif Mi?')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Silindi Mi?')),
                ('car_manager_mission_type_name', models.CharField(max_length=50, verbose_name='Araç Yöneticisi Görev Tip Adı')),
                ('description', models.CharField(blank=True, max_length=250, verbose_name='Açıklama')),
                ('joined_by_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)ss_%(class)s_related', related_query_name='%(app_label)ss_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan Kullanıcı')),
                ('modified_by_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Değiştiren Kullanıcı')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CarManager',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Değiştirilme Tarihi')),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktif Mi?')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Silindi Mi?')),
                ('description', models.CharField(blank=True, max_length=250, verbose_name='Açıklama')),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='r_car_of_manager', related_query_name='q_car_of_manager', to='car.car', verbose_name='Şöförün Kullanacağı Araç')),
                ('car_manager_mission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='r_mission_of_manager', related_query_name='q_mission_of_manager', to='car.carmanagermission', verbose_name='')),
                ('joined_by_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)ss_%(class)s_related', related_query_name='%(app_label)ss_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan Kullanıcı')),
                ('modified_by_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Değiştiren Kullanıcı')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='r_manager_of_car', related_query_name='q_manager_of_car', to=settings.AUTH_USER_MODEL, verbose_name='Araca Atanacak Şöför')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]