# Generated by Django 2.2.4 on 2020-02-22 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_attributs_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attributs',
            name='category',
        ),
        migrations.RemoveField(
            model_name='attributs',
            name='deep',
        ),
        migrations.RemoveField(
            model_name='deep',
            name='category',
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
        migrations.RemoveField(
            model_name='product',
            name='attributes',
        ),
        migrations.RemoveField(
            model_name='product',
            name='deep',
        ),
        migrations.DeleteModel(
            name='Attributs',
        ),
        migrations.DeleteModel(
            name='Deep',
        ),
    ]
