# Generated by Django 4.0.6 on 2022-07-16 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0003_alter_animal_cost_alter_animal_gain'),
        ('branch', '0002_branch_firm'),
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='r_branch_of_application', related_query_name='q_branch_of_application', to='branch.branch', verbose_name='Başvuru Yapılan Şube'),
        ),
        migrations.AlterField(
            model_name='application',
            name='animal_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='r_animal_type_of_application', related_query_name='q_animal_type_of_application', to='animal.animaltype', verbose_name='Hayvan Tipi'),
        ),
    ]
