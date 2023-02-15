from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class SocialNetwork(models.Model):
    name = models.CharField(max_length=50, verbose_name="name social network")
    url = models.URLField(max_length=500, verbose_name="url social network")
    url_image = models.URLField(max_length=500, verbose_name="image url")


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts")
