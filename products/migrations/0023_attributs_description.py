# Generated by Django 2.2.4 on 2019-11-03 11:13

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributs',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True, verbose_name='Текст'),
        ),
    ]
