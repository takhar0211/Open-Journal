from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title' , 'category' , 'author' , 'status' ,'is_featured', 'created_at' , 'updated_at')
    search_fields = ('title','category__category_name' , 'author__username' ,)
    list_filter =('status','is_featured','category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name' , 'created_at' , 'update_at')
    search_fields = ('category_name',)


admin.site.register(category,CategoryAdmin)
admin.site.register(blog,BlogAdmin)

