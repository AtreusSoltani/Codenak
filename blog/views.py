from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from blog.models import Post, Comment
from checklist.models import Solution


@login_required
def index(request):
    posts = Post.objects.order_by('-published_date').all()
    comments = Comment.objects.order_by('-published_date').all()

    def SolvedProblems(user):
        return Solution.objects.filter(username=user).count()

    topusers = sorted(User.objects.all(), key=SolvedProblems, reverse=True)[:10]
    topusers = [(user, len(Solution.objects.filter(username=user))) for user in topusers]

    return render(request, 'blog/main.html',
                  {'posts': posts,
                   'comments': comments,
                   'topusers': topusers,
                   })
