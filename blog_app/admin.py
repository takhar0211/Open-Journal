from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'blog_slug':('title',)}
    list_display = ('title' , 'category' , 'author' , 'status' ,'is_featured', 'is_hero' , 'updated_at')
    search_fields = ('title','category__category_name' , 'author__username' ,)
    list_filter =('status','is_featured','category')
    list_editable =('is_featured','is_hero')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name' , 'created_at' , 'update_at')
    search_fields = ('category_name',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(blog,BlogAdmin)

