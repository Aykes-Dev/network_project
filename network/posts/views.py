from django.shortcuts import render
from .models import SocialNetwork, Post


def index(request):
    a = range(29)
    posts = Post.objects.select_related('author').all()
    social_network = SocialNetwork.objects.all()
    content = {
        'a': a,
        'social_networks': social_network,
        'posts': posts,
    }
    return render(request, "posts/index.html", content)
