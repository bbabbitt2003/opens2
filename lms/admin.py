from django.contrib import admin
from .models import UserProfile, Project, Lesson, Test

admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Lesson)
admin.site.register(Test)

