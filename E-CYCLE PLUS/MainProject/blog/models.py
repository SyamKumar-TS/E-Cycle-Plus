from django.db import models

# Create your models here.
# models.py
from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField 
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=255, blank=True)
    content = RichTextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.title