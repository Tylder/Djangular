from django.contrib import admin
from profiles.models import *
# Register your models here.

# class TeacherAdmin(admin.ModelAdmin):
#
#     fieldsets = [
#         (None, {fields})
#     ]

admin.site.register(TeacherProfile)
admin.site.register(StudentProfile)