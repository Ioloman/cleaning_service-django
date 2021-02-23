# Generated by Django 3.1.7 on 2021-02-22 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('service_type_pk', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'SERVICE_TYPE',
            },
        ),
        migrations.CreateModel(
            name='UserService',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('user_service_pk', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('type', models.SmallIntegerField(choices=[(1, 'Частное лицо'), (2, 'Клининговое агенство')])),
                ('phone', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'USER_SERVICE',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('service_pk', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('service_type_pk', models.ForeignKey(db_column='service_type_pk', on_delete=django.db.models.deletion.RESTRICT, to='cleaning_app.servicetype')),
                ('user_service_pk', models.ForeignKey(db_column='user_service_pk', on_delete=django.db.models.deletion.CASCADE, to='cleaning_app.userservice')),
            ],
            options={
                'db_table': 'SERVICE',
                'unique_together': {('service_pk', 'user_service_pk', 'service_type_pk')},
            },
        ),
    ]
