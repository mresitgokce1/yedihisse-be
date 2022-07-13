# Generated by Django 4.0.6 on 2022-07-12 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='cattle_capacity',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Büyükbaş Kapasitesi'),
        ),
        migrations.AlterField(
            model_name='car',
            name='ovine_capacity',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Küçükbaş Kapasitesi'),
        ),
    ]
