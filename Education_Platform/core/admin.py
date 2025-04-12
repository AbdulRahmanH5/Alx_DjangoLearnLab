from django.contrib import admin
from . models import Course, Lesson, Profile, Enrollment, User

# Registeration My models .
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Profile)
admin.site.register(Enrollment)