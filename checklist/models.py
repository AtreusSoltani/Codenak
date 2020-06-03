from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Organization(models.Model):
    organization_name = models.CharField(max_length=60)
    website = models.URLField(blank=True)
    logo = models.URLField(blank=True)

    def __str__(self):
        return self.organization_name

class Contest(models.Model):
    contest_name = models.CharField(max_length=50)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    contest_judge = models.URLField(blank=True)
    published_date = models.DateTimeField()
    def __str__(self):
        return self.contest_name

class Problem(models.Model):
    problem_name = models.CharField(max_length=50)
    contest = models.ForeignKey('Contest', on_delete=models.CASCADE)
    solved = models.BooleanField(default=False)

    def __str__(self):
        return self.problem_name

class Solution(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return (self.username.username + '_' + self.problem.problem_name)