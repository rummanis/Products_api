# Generated by Django 3.2.8 on 2021-10-19 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_geeksmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='geeksmodel',
            name='image_link',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='geeksmodel',
            name='price',
            field=models.FloatField(default=4),
            preserve_default=False,
        ),
    ]
