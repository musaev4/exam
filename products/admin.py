from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product, Image, ProductAttribute, Tag


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'get_image')
    search_fields = ('title', 'category__title', 'tags__name')
    list_filter = ('title', 'category__title', 'tags__name')
    inlines = (ImageInline, ProductAttributeInline)

    def get_image(self, obj):
        image = obj.images.first()
        if image:
            return mark_safe('<img src="{}" width="100px" />'.format(image.image.url))
        return None

    get_image.short_description = 'Фото'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name',)