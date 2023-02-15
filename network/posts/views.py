from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.select_related('author').all()
    content = {
        'posts': posts,
    }
    return render(request, "posts/index.html", content)
