# Generated by Django 2.0.13 on 2020-03-16 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200314_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='description',
        ),
    ]
