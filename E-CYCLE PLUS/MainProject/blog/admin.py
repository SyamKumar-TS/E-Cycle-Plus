from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'published_date')
    list_filter = ('published_date',)
    search_fields = ('title', 'content')
    date_hierarchy = 'published_date'
    actions = ['publish_posts']
    
    def publish_posts(self, request, queryset):
        rows_updated = queryset.update(published_date=timezone.now())
        if rows_updated == 1:
            message_bit = "1 blog post was"
        else:
            message_bit = f"{rows_updated} blog posts were"
        self.message_user(request, f"{message_bit} successfully published.")
    
    publish_posts.short_description = "Publish selected posts"

admin.site.register(BlogPost, BlogPostAdmin)