from django.shortcuts import get_object_or_404, render
from .models import *
# Create your views here.
def home(request):
    category = Category.objects.all();
    featured_post = blog.objects.filter(is_featured = True,status =1)
    hero_post = blog.objects.filter(is_hero=True ,is_featured = False,status =1).first()
    recent_post = blog.objects.filter(is_featured = False,status =1,is_hero=False).order_by('-updated_at')[:6]
    context = {
        'category' : category,
        'featured_post':featured_post,
        'hero_post':hero_post,
        'recent_post':recent_post
    }
    return render(request,'home.html',context)

def category_page(request,slug):
    current_category = get_object_or_404(Category,slug=slug)
    
    posts = blog.objects.filter(
        category = current_category,
        status = 1,
    ).order_by('-created_at')

    categories = Category.objects.all()

    context = {
        'posts' : posts,
        'category':categories,
        'current_category':current_category,
    }
    return render(request,'category_page.html',context)