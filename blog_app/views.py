from django.shortcuts import render
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