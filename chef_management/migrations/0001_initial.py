# Generated by Django 5.0 on 2024-01-19 18:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('dish_id', models.IntegerField(primary_key=True, serialize=False)),
                ('dish_name', models.TextField()),
                ('dish_description', models.TextField(null=True)),
                ('dish_type', models.TextField()),
                ('calories', models.IntegerField(null=True)),
                ('light_healthy', models.BooleanField(null=True)),
                ('sugar_free', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DateHasDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chef_management.date')),
                ('dish_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chef_management.dish')),
            ],
        ),
    ]
