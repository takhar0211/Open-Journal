from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import *
# Create your views here.
def home(request):
    hero_post = blog.objects.filter(is_hero=True ,is_featured = False,status =1).first()
    recent_post = blog.objects.filter(is_featured = False,status =1,is_hero=False).order_by('-updated_at')[:6]
    context = {
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

    context = {
        'posts' : posts,
        'current_category':current_category,
    }
    return render(request,'category_page.html',context) 

def blogs(request,blog_slug):
    current_post = get_object_or_404(blog,blog_slug = blog_slug)

    return render(request,'blogs.html',{'post':current_post})