# Generated by Django 4.1 on 2022-08-18 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scholarship', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='image',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='mobile',
            field=models.CharField(default='0000000', max_length=12),
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(default='0000000', max_length=12)),
                ('image', models.FileField(upload_to='')),
                ('gender', models.CharField(max_length=10)),
                ('companyname', models.CharField(max_length=50)),
                ('usertype', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
