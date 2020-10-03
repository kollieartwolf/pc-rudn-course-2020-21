from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.opened.all()
    return render(request,
                  'post/list.html',
                  {'posts': posts})


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post,
                             status='opened')
    return render(request,
                  'post/lecture.html',
                  {'post': post})
