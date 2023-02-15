from django.contrib import admin
from .models import SocialNetwork, Post


# Register your models here.
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'url',
        'url_image',
    )
    empty_value_display = '-пусто-'


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'text',
        'author',
        'pub_date',
    )
    empty_value_display = '-пусто-'


admin.site.register(SocialNetwork, SocialNetworkAdmin)
admin.site.register(Post, PostAdmin)
