# Generated by Django 2.2.4 on 2019-09-24 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filters', '0015_auto_20190924_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productfilter',
            name='values',
        ),
    ]
