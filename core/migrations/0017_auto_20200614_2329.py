# Generated by Django 3.0.7 on 2020-06-14 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_blogpost_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(upload_to='pics'),
        ),
    ]