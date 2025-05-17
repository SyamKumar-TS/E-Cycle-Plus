# urls.py
from django.urls import path
from .views import *
from . import views  
urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('admin/blogs/', views.admin_blog_list, name='admin_blog_list'),
    path('admin/blogs/new/', views.admin_blog_create, name='admin_blog_create'),
    path('admin/blogs/<int:pk>/edit/', views.admin_blog_edit, name='admin_blog_edit'),
    path('admin/blogs/<int:pk>/delete/', views.admin_blog_delete, name='admin_blog_delete'),
]