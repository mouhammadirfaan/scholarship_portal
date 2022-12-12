# Generated by Django 4.1 on 2022-12-11 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0043_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applyscholarship',
            name='addscholarship',
        ),
        migrations.RemoveField(
            model_name='applyscholarship',
            name='student',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='user',
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='AddScholarship',
        ),
        migrations.DeleteModel(
            name='ApplyScholarship',
        ),
        migrations.DeleteModel(
            name='Provider',
        ),
        migrations.DeleteModel(
            name='StudentUser',
        ),
    ]
