# Generated by Django 2.1.5 on 2019-01-09 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_post_createdat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='createdAt',
        ),
    ]
