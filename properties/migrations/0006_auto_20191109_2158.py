# Generated by Django 2.2.4 on 2019-11-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_auto_20191109_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryproperty',
            name='name',
            field=models.CharField(blank=True, default='', max_length=250, unique=True),
        ),
    ]
