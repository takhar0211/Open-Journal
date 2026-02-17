from django.db import models

class category(models.Model):
    category_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # to make the name correct in admin pannel because its automatically add a 's' to the models
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name
    

class blog(models.Model):
    b