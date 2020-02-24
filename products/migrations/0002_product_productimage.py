# Generated by Django 2.2.4 on 2019-08-13 22:33

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=120, null=True)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to=products.models.image_folder)),
                ('slug', models.SlugField(blank=True, default=None, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('price_old', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('description', models.CharField(blank=True, default=None, max_length=120, null=True)),
                ('description_short', models.CharField(blank=True, default=None, max_length=120, null=True)),
                ('discount', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('new_product', models.BooleanField(default=False)),
                ('top', models.BooleanField(default=False)),
                ('comments', models.TextField(blank=True, default=None, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('categ', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='products.Category')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images/')),
                ('is_main', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
