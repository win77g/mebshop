# Generated by Django 2.2.4 on 2019-08-30 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20190825_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinorder',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
