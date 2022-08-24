# Generated by Django 4.1 on 2022-08-24 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0008_provider'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddScholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('logo', models.FileField(upload_to='')),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('noofscholarships', models.IntegerField()),
                ('Location', models.CharField(max_length=256)),
                ('scholarshiptype', models.CharField(max_length=100)),
                ('prviousmarks', models.CharField(max_length=100)),
                ('income', models.CharField(max_length=100, null=True)),
                ('createdate', models.DateField()),
                ('discription', models.TextField()),
                ('procider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scholarship.provider')),
            ],
        ),
    ]
