# Generated by Django 4.1 on 2022-08-18 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0003_alter_studentuser_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='mobile',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='mobile',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
