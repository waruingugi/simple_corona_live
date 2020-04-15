# Generated by Django 2.2.7 on 2020-04-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(blank=True, max_length=10, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'User',
            },
        ),
    ]
