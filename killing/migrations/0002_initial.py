# Generated by Django 4.0.6 on 2022-07-13 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('killing', '0001_initial'),
        ('slaughterhouse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='killinggroup',
            name='slaughterhouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='r_slaughterhouse_of_killing_group', related_query_name='q_slaughterhouse_of_killing_group', to='slaughterhouse.slaughterhouse', verbose_name='Kesim Grubunun Kesimhanesi'),
        ),
    ]