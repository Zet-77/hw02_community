from django.conf import settings
from django.shortcuts import get_object_or_404, render
from .models import Group, Post


def index(request):
    posts = Post.objects.order_by('-pub_date')[:settings.LIMIT]
    title = 'Главная страница'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:settings.LIMIT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
