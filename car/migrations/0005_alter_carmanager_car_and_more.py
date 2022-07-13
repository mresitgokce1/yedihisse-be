# Generated by Django 4.0.6 on 2022-07-12 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car', '0004_carmanagermission_carmanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmanager',
            name='car',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='r_car_of_manager', related_query_name='q_car_of_manager', to='car.car', verbose_name='Görevlinin Atanacağı Araç'),
        ),
        migrations.AlterField(
            model_name='carmanager',
            name='car_manager_mission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='r_mission_of_manager', related_query_name='q_mission_of_manager', to='car.carmanagermission', verbose_name='Araç Görevlisinin Görevi'),
        ),
        migrations.AlterField(
            model_name='carmanager',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='r_manager_of_car', related_query_name='q_manager_of_car', to=settings.AUTH_USER_MODEL, verbose_name='Araca Atanacak Görevli'),
        ),
        migrations.AlterField(
            model_name='carmanagermission',
            name='car_manager_mission_type_name',
            field=models.CharField(max_length=50, verbose_name='Araç Görevlisinin Görev Tip Adı'),
        ),
    ]