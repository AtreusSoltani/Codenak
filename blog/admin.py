from django.contrib import admin

from blog import models
from blog.models import Comment, Post

admin.site.register(Post)
admin.site.register(Comment)
