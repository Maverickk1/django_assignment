# Generated by Django 3.1.4 on 2021-09-11 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentdata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
    ]
