# Generated by Django 3.2.9 on 2022-01-29 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmodel',
            old_name='address',
            new_name='city',
        ),
    ]