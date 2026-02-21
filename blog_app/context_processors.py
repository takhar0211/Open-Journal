from .models import *

def get_category(request):
    categories = Category.objects.all()
    return dict(categories = categories)

def get_featured_posts(request):
    featured_posts = blog.objects.filter(is_featured = True,status = 1)
    return dict(featured_posts = featured_posts)