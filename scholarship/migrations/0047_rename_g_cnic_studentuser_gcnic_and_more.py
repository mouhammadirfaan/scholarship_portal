# Generated by Django 4.1 on 2022-12-11 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0046_rename_total_income_studentuser_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentuser',
            old_name='g_cnic',
            new_name='gcnic',
        ),
        migrations.RenameField(
            model_name='studentuser',
            old_name='g_name',
            new_name='gname',
        ),
        migrations.RenameField(
            model_name='studentuser',
            old_name='i_type',
            new_name='itype',
        ),
    ]
