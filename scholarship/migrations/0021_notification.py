# Generated by Django 4.1 on 2022-10-28 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0020_delete_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(choices=[('message', 'Message')], max_length=20)),
                ('is_read', models.BooleanField(default=False)),
                ('extra_id', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('upload_scholarship_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scholarship.addscholarship')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
