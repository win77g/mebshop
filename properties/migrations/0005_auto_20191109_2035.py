# Generated by Django 2.2.4 on 2019-11-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_auto_20191109_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryproperty',
            name='name',
            field=models.CharField(default='', max_length=250, unique=True),
        ),
    ]
