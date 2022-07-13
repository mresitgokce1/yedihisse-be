# Generated by Django 4.0.6 on 2022-07-13 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car', '0005_alter_carmanager_car_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmanager',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r_car_of_manager', related_query_name='q_car_of_manager', to='car.car', verbose_name='Görevlinin Atanacağı Araç'),
        ),
        migrations.AlterField(
            model_name='carmanager',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r_manager_of_car', related_query_name='q_manager_of_car', to=settings.AUTH_USER_MODEL, verbose_name='Araca Atanacak Görevli'),
        ),
    ]