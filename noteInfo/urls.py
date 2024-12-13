from django.urls import path
from .import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_details, name='blog-details'),
     path('blog-search/', views.search_blog, name='search_blog')
]