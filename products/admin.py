from django.contrib import admin
from .models import *
from metatags.admin import MetaTagInline
from properties.models import CategoryProperty, ProductProperty
from filters.models import FilterCategory, ProductFilter, FilterSelect
from django.forms import TextInput, ModelForm, Textarea, Select
# Register your models here.
#----------------------------------------------------------
class CategoryPropertyInline(admin.TabularInline):
    model = CategoryProperty
    extra = 1
    verbose_name_plural = 'Params'
    suit_classes = 'suit-tab suit-tab-params'

class ProductPropertyInline(admin.TabularInline):
    model = ProductProperty
    extra = 1
    verbose_name_plural = 'Params'
    suit_classes = 'suit-tab suit-tab-params'

class ProductFilterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductFilterForm, self).__init__(*args, **kwargs)
        if self.instance:
            i = self.instance
            if i.filter_category:
                self.fields["values"].queryset =\
                 FilterSelect.objects.filter(filter_category=i.filter_category)
            else:
                self.fields["values"].queryset =\
                 FilterSelect.objects.all()[:1]

    class Meta:
        model = ProductFilter
        fields = '__all__'

class ProductFilterInline(admin.TabularInline):
    form = ProductFilterForm
    # filter_horizontal = ('values', )
    model = ProductFilter
    extra = 0
    verbose_name_plural = 'Filters'
    suit_classes = 'suit-tab suit-tab-filters'

class FilterCategoryInline(admin.TabularInline):
    model = FilterCategory
    extra = 0
    verbose_name_plural = 'Filters'
    suit_classes = 'suit-tab suit-tab-filters'

    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }



# ----------------------------Category----------------------------------------------------------
class CategoryAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Category._meta.fields]
      # add meatateg fields
      inlines = (MetaTagInline,)
      class Meta:
           model = Category
      def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }
# Register your models here.
admin.site.register(Category, CategoryAdmin)


# class ProductCategoryAdmin (admin.ModelAdmin):
#    #  вывод всех полей в админку
#       list_display = [field.name for field in ProductCategory._meta.fields]
#
#       class Meta:
#            model = ProductCategory
# # Register your models here.
# admin.site.register(ProductCategory, ProductCategoryAdmin)
# ----------------------------END Category----------------------------------------------------------

# ----------------------------Attributs--------------------------------------------------------------
# class AttributsAdmin (admin.ModelAdmin):
#    #  вывод всех полей в админку
#       list_display = [field.name for field in Attributs._meta.fields]
#
#       class Meta:
#            model = Attributs
# # Register your models here.
# admin.site.register(Attributs, AttributsAdmin)
# ----------------------------END Attributs--------------------------------------------------------------

# ----------------------------Deep--------------------------------------------------------------
# class DeepAdmin (admin.ModelAdmin):
#    #  вывод всех полей в админку
#       list_display = [field.name for field in Deep._meta.fields]
#
#       class Meta:
#            model = Deep
# # Register your models here.
# admin.site.register(Deep, DeepAdmin)
# ----------------------------END Deep--------------------------------------------------------------

# ----------------------------Brend--------------------------------------------------------------
class BrendAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Brend._meta.fields]

      class Meta:
           model = Brend
# Register your models here.
admin.site.register(Brend, BrendAdmin)
# ----------------------------END Brend--------------------------------------------------------------

# ----------------------------Gallery----------------------------------------------------------
#добавление фоток внизу прдукт админки
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    list_display = ['image_img',]
    readonly_fields = ['image_img',]
# ---------------------------- end Gallery----------------------------------------------------------

# ----------------------------Product----------------------------------------------------------
# Register your models here.
class ProductAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
   #    list_display = [field.name for field in Product._meta.fields]
   inlines = [ProductImageInline,MetaTagInline,ProductPropertyInline,ProductFilterInline,]
   list_display = ('name','brend','categ','image_img', 'price','is_active','new_product','top','slider')
   readonly_fields = ['image_img',]
   # verbose_name_plural = 'Main'
   search_fields = ["price","name","brend__name"]
   list_filter = ['categ','brend','is_active','new_product','top']
   # suit_form_tabs = (
   #      ('main', 'Main'),
   #      ('params', 'Params'),
   #      ('filters','Filters'),)
   # fieldsets = [('Main',{
   #                   'classes': ('suit-tab', 'suit-tab-main',),
   #                   'fields':[
   #         'name','brend','categ','attributes','description','description_short','image_img', 'price','is_active','new_product','top','slider'
   #                   ]
   #                       }
   #               )]
   list_per_page = 15

   # ------------


   # meta

   # inlines = (MetaTagInline,)

   # def formfield_for_manytomany(self, db_field, request=None, **kwargs):
   #      if db_field.name == 'membership':
   #          qs = kwargs.get('queryset', db_field.remote_field.model.objects)
   #          # Avoid a major performance hit resolving membership names which
   #          # triggers a content_type load:
   #          kwargs['queryset'] = qs.select_related('content_type')
   #      return super().formfield_for_manytomany(db_field, request=request, **kwargs)
   # fields = ['category', 'title', 'slug', 'metakey', 'metadesc', 'text_redactor', 'text_redactor_full', 'tag', 'timestamp', 'autor', 'image', 'image_img', 'body', 'likes', 'dislikes']

class Meta:
    model = Product
# Register your models here.
admin.site.register(Product,ProductAdmin)
# ----------------------------END Product----------------------------------------------------------
