# blog/views.py
from django.shortcuts import render

from django.views.generic import ListView, DetailView # new

from django.views.generic.edit import CreateView, UpdateView # new

from .models import Post

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'

class BlogDetailView(DetailView): # new
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'indiv_post'

class BlogCreateView(CreateView): # new
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView): # new
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

