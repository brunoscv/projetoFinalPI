# Generated by Django 2.1.5 on 2019-01-09 14:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='createdAt',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]