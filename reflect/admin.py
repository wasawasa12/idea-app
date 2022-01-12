from django.contrib import admin
from .models import ReflectIssues, ReflectContents, ReflectProblem
# Register your models here.
admin.site.register(ReflectIssues)
admin.site.register(ReflectContents)
admin.site.register(ReflectProblem)
