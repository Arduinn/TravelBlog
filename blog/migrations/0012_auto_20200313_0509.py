# Generated by Django 2.0.13 on 2020-03-13 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200313_0450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='height',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='width',
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='imagens/'),
        ),
    ]
