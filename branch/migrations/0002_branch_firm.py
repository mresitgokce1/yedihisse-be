# Generated by Django 4.0.6 on 2022-07-13 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firm', '0001_initial'),
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='firm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='r_firm_of_branch', related_query_name='q_firm_of_branch', to='firm.firm', verbose_name='Şubenin Firması'),
        ),
    ]
