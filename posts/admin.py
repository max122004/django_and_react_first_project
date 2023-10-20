from django.contrib import admin
from django.contrib.admin import ModelAdmin

from posts.models import Posts


@admin.register(Posts)
class PostsAdmin(ModelAdmin):
    pass