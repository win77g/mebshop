from django.contrib import admin
from .models import FilterCategory, FilterSelect, ProductFilter



class FilterSelectInline(admin.TabularInline):
    model = FilterSelect
    extra = 1
    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }



@admin.register(FilterCategory)
class FilterCategoryAdmin(admin.ModelAdmin):
    inlines = [FilterSelectInline, ]
    list_display = ('name','slug','category')


    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }

@admin.register(FilterSelect)
class FilterSelectAdmin(admin.ModelAdmin):
    list_display = ('name','slug','category','filter_category','simple')
    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }


@admin.register(ProductFilter)
class ProductFilterAdmin(admin.ModelAdmin):
    list_display = ('product','filter_category','values','simple')
    #pass
