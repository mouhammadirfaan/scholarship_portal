# Generated by Django 4.1 on 2022-12-11 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0050_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentuser',
            name='cnic',
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='disability',
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='end',
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='gcnic',
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='gname',
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='institution',
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='itype',
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='registration',
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='religion',
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='start',
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='total',
        ),
    ]
