# Generated by Django 4.0.6 on 2022-07-13 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('phone', '0002_initial'),
        ('address', '0003_alter_district_linked_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Değiştirilme Tarihi')),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktif Mi?')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Silindi Mi?')),
                ('branch_name', models.CharField(max_length=50, verbose_name='Şube Adı')),
                ('address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='address.address', verbose_name='Şube Adresi')),
                ('joined_by_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)ss_%(class)s_related', related_query_name='%(app_label)ss_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan Kullanıcı')),
                ('modified_by_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Değiştiren Kullanıcı')),
                ('phone', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='phone.phonenumber', verbose_name='Şube Telefonu')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BranchManagerMission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Değiştirilme Tarihi')),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktif Mi?')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Silindi Mi?')),
                ('branch_manager_mission_type_name', models.CharField(max_length=50, verbose_name='Şube Görevlisi Görev Tip Adı')),
                ('description', models.CharField(blank=True, max_length=250, verbose_name='Açıklama')),
                ('joined_by_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)ss_%(class)s_related', related_query_name='%(app_label)ss_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan Kullanıcı')),
                ('modified_by_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Değiştiren Kullanıcı')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BranchManager',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Değiştirilme Tarihi')),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktif Mi?')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Silindi Mi?')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='Açıklama')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r_branch_of_manager', related_query_name='q_branch_of_manager', to='branch.branch', verbose_name='Görevliye Atanan Şube')),
                ('branch_manager_mission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='r_mission_of_manager', related_query_name='q_mission_of_manager', to='branch.branchmanagermission')),
                ('joined_by_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)ss_%(class)s_related', related_query_name='%(app_label)ss_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan Kullanıcı')),
                ('modified_by_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Değiştiren Kullanıcı')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r_manager_of_branch', related_query_name='q_manager_of_branch', to=settings.AUTH_USER_MODEL, verbose_name='Şubeye Atanacak Görevli')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]