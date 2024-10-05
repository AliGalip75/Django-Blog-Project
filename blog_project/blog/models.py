from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, editable=False)
    is_active = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)  
        
    def __str__(self):
        return self.name  
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=50, default="")
    slug = models.SlugField(editable=True, blank=True, null=False, unique=True)#blank formda slug bilgisi girmek zorunda kalmayalım diye
    content = models.TextField()
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE, related_name="posts")
    published_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    image = models.ImageField(null=True, upload_to='posts/images/')
    is_active = models.BooleanField(default=1)
    
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
          
    def save(self, *args, **kwargs):
        
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)    
    
    def __str__(self):
        return self.title
    