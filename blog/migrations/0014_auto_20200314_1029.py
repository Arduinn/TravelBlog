# Generated by Django 2.0.13 on 2020-03-14 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200313_0511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='desc',
            new_name='description',
        ),
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
