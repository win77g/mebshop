# Generated by Django 2.2.4 on 2019-11-16 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filters', '0032_auto_20191116_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='filterselect',
            name='simple',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
