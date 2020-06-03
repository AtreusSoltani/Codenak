from django.contrib import admin
from .models import Organization, Problem, Contest
# Register your models here.

admin.site.register(Organization)
admin.site.register(Problem)
admin.site.register(Contest)