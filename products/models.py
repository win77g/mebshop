from django.db import models
from properties.models import ProductProperty, CategoryProperty
from filters.models import ProductFilter, FilterCategory
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models.signals import  pre_save
# преврашает в slug
from django.utils.text import slugify
# переводит кирилицу в латынь
from transliterate import translit
from ckeditor_uploader.fields import RichTextUploadingField
import os
from django.dispatch import receiver
# Create your models here.
# 1.Category
# 2.Attrebut
# 3.Brend
# 4.Product
# 5.Gallery
# -----------------------------------Category-------------------------------------------------
class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children',verbose_name="Родитель", db_index=True,on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name='Транслит', null = True)
    description = RichTextUploadingField(verbose_name='Текст',blank=True, null=True, default=None)

    def __str__(self):
        return " %s" % self.name

    class MPTTMeta:
        order_insertion_by = ['name']

# модель категории
# class ProductCategory(models.Model):
#     name_category = models.CharField(max_length=120, blank=True, null=True, default=None)
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return " %s" % self.name_category
#     class Meta:
#         verbose_name = 'Категория товара'
#         verbose_name_plural = 'Категория товаров'
# ---------------------------------end Category-------------------------------------------------------------

# ------------------------------модель Deep---------------------------------------------------
# class Deep(models.Model):
#     name = models.CharField(max_length=120,blank=True, null=True, default=None,verbose_name='Глубина')
#     category = models.ForeignKey(Category,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Категория')
#
#     # вывод одного поля
#     def __str__(self):
#         return " %s" % self.name
#     class Meta:
#         verbose_name = 'Размер(глубина)'
#         verbose_name_plural = 'Размер(глубина)'
#
# ----------------------------------end deep--------------------------------------------


# ------------------------------модель Attributs---------------------------------------------------
# class Attributs(models.Model):
#     name = models.CharField(max_length=50,blank=True, null=True, default=None,verbose_name='Название')
#     deep = models.ForeignKey(Deep,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Глубина')
#     category = models.ForeignKey(Category,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Категория')
#     slug = models.SlugField(blank=True, null=True, default=None , verbose_name='Транслит')
#     description = RichTextUploadingField(verbose_name='Текст',blank=True, null=True, default=None)
#     # вывод одного поля
#     def __str__(self):
#         return " %s" % self.name
#     class Meta:
#         verbose_name = 'Атрибут'
#         verbose_name_plural = 'Атрибуты'
# # автоматическое сохранение поля слаг в бренд
# def pre_save_attributes_slug(sender,instance, *args, **kwargs):
#     if not instance.slug:
#         slug = slugify(translit(instance.name, reversed=True))
#         instance.slug = slug
# pre_save.connect(pre_save_attributes_slug, sender=Attributs)
# ----------------------------------end attributs--------------------------------------------------------



# ------------------------------модель Бренда---------------------------------------------------
class Brend(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True, default=None)
    slug = models.SlugField(blank=True, null=True, default=None ,verbose_name='Транслит')
    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренд'
# автоматическое сохранение поля слаг в бренд
def pre_save_brend_slug(sender,instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.name, reversed=True))
        instance.slug = slug
pre_save.connect(pre_save_brend_slug, sender=Brend)
# ----------------------------------end brend--------------------------------------------------------

# ---------------------------------Product---------------------------------------------------
# создание названия фотки
def image_folder(instance,filename):
    filename = instance.slug +'.'+filename.split('.')[1]
    return "{0}/{1}".format(instance.slug,filename)


# модеь продукта
class Product(models.Model):
    name = models.CharField(verbose_name='Название',max_length=120,blank=True, null=True)
    brend = models.ForeignKey(Brend,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Бренд')
    categ = TreeForeignKey(Category, blank=True, null=True,related_name = 'cat',on_delete=models.CASCADE,verbose_name='Категория')
    # attributes = models.ForeignKey(Attributs,max_length=20,blank=True, null=True,on_delete=models.CASCADE,verbose_name='Подкатегория')
    # deep = models.ForeignKey(Deep,max_length=10,blank=True, null=True,on_delete=models.CASCADE,verbose_name='Глубина')
    image = models.ImageField(upload_to=image_folder, blank=True, null=True, default=None,verbose_name='Фотка')
    slug = models.SlugField(blank=True, null=True, default=None,verbose_name='Транслит(Не трогать)')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='Цена')
    price_old = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='Старая цена')
    # description = RichTextUploadingField(config_name='default')
    # description_short = RichTextUploadingField(config_name='default')
    description = RichTextUploadingField(verbose_name='Текст',blank=True, null=True, default=None)
    description_short = RichTextUploadingField(verbose_name='Текст(короткий)',blank=True, null=True, default=None)
    discount = models.IntegerField(default=0,verbose_name='Скидка')
    # category = models.ForeignKey(ProductCategory,blank=True, null=True, default=None )

    is_active = models.BooleanField(default=True,verbose_name='В наличии')
    new_product = models.BooleanField(default=False,verbose_name='Новинка')
    top = models.BooleanField(default=False,verbose_name='В топе(на гл.странице)')
    slider = models.BooleanField(default=False,verbose_name='Слайдер(на гл.странице)')
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=False,auto_now=True,verbose_name='Дата последнего обновления')
    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    def save(self, *args, **kwargs):
        if self.categ:
            super(Product, self).save(*args, **kwargs)
            # we create properties if not exist
            for cp in CategoryProperty.objects.filter(category=self.categ):
                pp = ProductProperty.objects.filter(category_property=cp,
                    product=self)
                if not pp:
                    pp = ProductProperty(category_property=cp, product=self, value="--")
                    pp.save()
            # we create filters if not exist
            for fc in FilterCategory.objects.filter(category=self.categ):
                pf = ProductFilter.objects.filter(filter_category=fc,
                    product=self)
                if not pf:
                    pf = ProductFilter(filter_category=fc, product=self)
                    pf.save()

    def image_img(self):
        if self.image:
            return mark_safe(u'<a href="{0}"target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True
# удаление фото

# автоматическое сохранение поля слаг в продуктах
def pre_save_product_slug(sender,instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.name, reversed=True))
        instance.slug = slug
pre_save.connect(pre_save_product_slug, sender=Product)
# -----------------------------end product-------------------------------------------------------------


#  --------------------------Gallery-------------------------------------------------------
# создание названия фотки
def image_gallary_folder(instance,filename):
    filename = instance.slug +'.'+filename.split('.')[1]
    return "{0}/{1}".format(instance.slug,filename)
# фотки продукта
class ProductImage(models.Model):
    product = models.ForeignKey(Product,blank=True, null=True, default=None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to= image_gallary_folder,blank=True, null=True, default=None)
    slug = models.SlugField(blank=True, null=True, default=None , verbose_name='Транслит')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def image_img(self):
        if self.image:
            return mark_safe(u'<a href="{0}"target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

# автоматическое сохранение поля слаг в gallery
def pre_save_imagegallery_slug(sender,instance, *args, **kwargs):
    # print(instance.filename)
    if not instance.slug:
        slug = slugify(translit(instance.product.name, reversed=True))
        instance.slug = slug
pre_save.connect(pre_save_imagegallery_slug, sender=ProductImage)
# ---------------------------------------end gallery----------------------------------
