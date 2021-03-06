# Generated by Django 4.0.6 on 2022-07-12 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0001_initial'),
        ('phone', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cartype',
            name='joined_by_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)ss_%(class)s_related', related_query_name='%(app_label)ss_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan Kullanıcı'),
        ),
        migrations.AddField(
            model_name='cartype',
            name='modified_by_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Değiştiren Kullanıcı'),
        ),
        migrations.AddField(
            model_name='carmissiontype',
            name='joined_by_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)ss_%(class)s_related', related_query_name='%(app_label)ss_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan Kullanıcı'),
        ),
        migrations.AddField(
            model_name='carmissiontype',
            name='modified_by_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Değiştiren Kullanıcı'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_mission_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='r_mission_of_car', related_query_name='q_mission_of_car', to='car.carmissiontype', verbose_name='Araç Görev Tipi'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='r_type_of_car', related_query_name='q_type_of_car', to='car.cartype', verbose_name='Araç Tipi'),
        ),
        migrations.AddField(
            model_name='car',
            name='joined_by_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)ss_%(class)s_related', related_query_name='%(app_label)ss_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan Kullanıcı'),
        ),
        migrations.AddField(
            model_name='car',
            name='modified_by_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Değiştiren Kullanıcı'),
        ),
        migrations.AddField(
            model_name='car',
            name='phone_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='r_phone_of_car', related_query_name='q_phone_of_car', to='phone.phonenumber', verbose_name='Aracın numarası'),
        ),
    ]
