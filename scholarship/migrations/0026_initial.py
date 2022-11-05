# Generated by Django 4.1 on 2022-11-05 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scholarship', '0025_remove_applyscholarship_addscholarship_and_more'),
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
                ('discription', models.TextField()),
                ('createdate', models.DateField()),
                ('scholarshipform', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('image', models.FileField(upload_to='')),
                ('gender', models.CharField(max_length=10)),
                ('usertype', models.CharField(max_length=30)),
                ('currentdegree', models.CharField(max_length=100)),
                ('previousmarks', models.CharField(blank=True, max_length=100)),
                ('income', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('discriotion', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=12)),
                ('image', models.FileField(upload_to='')),
                ('gender', models.CharField(max_length=10)),
                ('companyname', models.CharField(max_length=50)),
                ('usertype', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApplyScholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scholarshipform', models.FileField(blank=True, upload_to='')),
                ('applyeddate', models.DateField()),
                ('addscholarship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scholarship.addscholarship')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scholarship.studentuser')),
            ],
        ),
        migrations.AddField(
            model_name='addscholarship',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scholarship.provider'),
        ),
    ]
