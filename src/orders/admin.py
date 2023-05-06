from django.contrib import admin
from .models import Photo, Orders, Category


class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'description',
        'slug',
        'price',
        'time_create',
        'time_update', 
        'photo_id',
        'is_active',
        'cat'
    )
    list_display_links = (
        'pk',
        'title',
        'photo_id',
        'slug',
        'cat'
    )
    list_editable = ('is_active',)
    search_fields = ('pk', 'title', 'cat')
    prepopulated_fields = {'slug': ('title',)}


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'photo', 'sender', 'custom')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug', 'is_active')
    list_display_links = ('pk', 'slug')
    search_fields = ('slug',)
    prepopulated_fields = {'slug': ('name',)}

    

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Category, CategoryAdmin)
