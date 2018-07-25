from django.contrib import admin

from courses.models import Course, Module, Lesson, Employer

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(Employer)
