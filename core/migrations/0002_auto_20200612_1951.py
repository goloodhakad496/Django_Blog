# Generated by Django 3.0.7 on 2020-06-12 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_of_publish',
            field=models.DateField(auto_now_add=True),
        ),
    ]
