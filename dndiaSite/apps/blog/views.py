from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q

from .models import *


def blog(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(title__icontains=search_query))

    else:
        posts = Post.objects.all()


    tags = Tag.objects.all()
    paginator = Paginator(posts, 2)
    page_num = request.GET.get('page', 1)


    page = paginator.get_page(page_num)
    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''



    return render(request, 'blog/blog.html', {'posts': page, 'tags': tags, 'is_paginated': is_paginated, 'prev_url':prev_url, 'next_url':next_url})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', {'post': post})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', {'tag': tag})
