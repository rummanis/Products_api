# Generated by Django 3.2.8 on 2021-10-19 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_auto_20211019_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='geeksmodel',
            name='bal',
            field=models.CharField(default=7, max_length=200),
            preserve_default=False,
        ),
    ]
