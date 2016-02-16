from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts':posts} )

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, 
            slug=post, 
            status='published',
            publish__year=year,
            publish__month=month,
            publish_day=day)
    return render(request, 'blog/post/detail.html', {'post':post})


