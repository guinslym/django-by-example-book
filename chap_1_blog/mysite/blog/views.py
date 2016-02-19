from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, \
        PageNotAnInteger

from .models import Post

# Create your views here.

def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 1) # 3 post in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #if page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        #if page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html',
            {'page': page,
                'posts':posts}
            )


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, 
            slug=post, 
            status='published',
            publish__year=year,
            publish__month=month,
            publish__day=day)
    return render(request, 'blog/post/detail.html', {'post':post})


