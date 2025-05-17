from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import BlogPost
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from .models import BlogPost
from .forms import BlogPostForm

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'  # Update this line
    context_object_name = 'blogs'
    ordering = ['-published_date']
    paginate_by = 6

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'  # Update this line
    context_object_name = 'blog'
@login_required
def admin_blog_list(request):
    blogs = BlogPost.objects.all().order_by('-created_date')
    return render(request, 'admin/blog/blog_list.html', {'blogs': blogs})

@login_required
def admin_blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.published_date = timezone.now()
            blog_post.save()
            messages.success(request, 'Blog post created successfully!')
            return redirect('admin_blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'admin/blog/blog_form.html', {'form': form})

@login_required
def admin_blog_edit(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.save()
            messages.success(request, 'Blog post updated successfully!')
            return redirect('admin_blog_list')
    else:
        form = BlogPostForm(instance=blog_post)
    return render(request, 'admin/blog/blog_form.html', {'form': form, 'blog': blog_post})

@login_required
def admin_blog_delete(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        blog_post.delete()
        messages.success(request, 'Blog post deleted successfully!')
        return redirect('admin_blog_list')
    return render(request, 'admin/blog/blog_confirm_delete.html', {'blog': blog_post})