# Generated by Django 5.0 on 2024-01-30 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datehasdish',
            old_name='date',
            new_name='date_saved',
        ),
    ]
