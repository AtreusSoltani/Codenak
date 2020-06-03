from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Organization, Contest, Problem, Solution


# Create your views here.
@login_required
def index(request):
    q = request.GET.get('query')
    if q is not None:
        u = request.user
        for problem_id in q.split(','):
            problem = Problem.objects.get(id=problem_id)
            usersols = Solution.objects.filter(username=u, problem=problem)
            if (usersols.count() == 1):
                instance = usersols[0]
                instance.delete()
            else:
                instance = Solution.objects.create(username=u, problem=problem)
                instance.save()
        return redirect('/checklist')

    organizations = Organization.objects.order_by('organization_name').all()
    problems = list(Problem.objects.all())
    for i in range(len(problems)):
        if Solution.objects.filter(username=request.user, problem=problems[i]).count() == 1:
            problems[i] = (problems[i], True)
        else:
            problems[i] = (problems[i], False)
    return render(request, 'checklist/index.html',
                  {'organizations': organizations,
                   'problems': problems,
                   })
