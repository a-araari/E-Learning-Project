# Generated by Django 3.0.3 on 2020-03-14 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20200314_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='thumbnail',
        ),
        migrations.AlterField(
            model_name='chapter',
            name='slug',
            field=models.SlugField(),
        ),
    ]
