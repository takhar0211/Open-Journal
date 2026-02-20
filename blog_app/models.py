from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)

    # to make the name correct in admin pannel because its automatically add a 's' to the models
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name
    
STATUS_CHOICES =(
    (0,"Draft"),
    (1,"Published")
)

class blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200 ,unique= True , blank=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='upload/%Y/%m/%d')
    short_desc = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    status = models.IntegerField(choices=STATUS_CHOICES,default=0)
    is_featured = models.BooleanField(default=False)
    is_hero = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.is_hero:
            blog.objects.filter(is_hero=True).update(is_hero=False)
        super().save(*args, **kwargs)