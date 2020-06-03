from django.contrib.auth.models import User
from django.contrib.humanize.templatetags import humanize
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField()

    @property
    def get_date(self):
        return humanize.naturaltime(self.published_date)


class Comment(models.Model):
    parent = models.ForeignKey('Post', on_delete=models.CASCADE)
    body = models.TextField()
