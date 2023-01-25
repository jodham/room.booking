# Generated by Django 4.1.5 on 2023-01-25 00:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=150)),
                ('institution_email', models.EmailField(max_length=254)),
                ('motto', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=50)),
                ('vision', models.TextField()),
                ('mission', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Boooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_users', models.IntegerField()),
                ('time_booked', models.DateTimeField(default=django.utils.timezone.now)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
