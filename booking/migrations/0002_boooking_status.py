# Generated by Django 4.1.5 on 2023-01-25 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boooking',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]