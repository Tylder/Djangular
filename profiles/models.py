from django.db import models
from django.conf import settings

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.models import Group
'''
    A client signs up on the main page and is then sent a confirmation email.
    After confirming that email, the client becomes a user. 
    The user account has been given a user_role and depending on the user role 
    they are taken to different profile signup pages where they fill in the 
    remaining info and creates a teacher or student profile.
'''

class TeacherManager(models.Manager):

    def create(self, **kwargs):

        return super().create(**kwargs)

class BaseProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_name_or_username(self):    # prio 1 is full name
        name = self.user.get_full_name()
        if name:
            return name
        else:
            return self.user.username

    def __str__(self):
        return self.get_name_or_username()

    class Meta:
        abstract = True


class TeacherProfile(BaseProfile):

    base_salary = models.DecimalField(verbose_name="Base Salary",
                                      max_digits=5,
                                      decimal_places=1,
                                      default=0)

    rank = models.PositiveSmallIntegerField(default=0)

    lessons_conducted = models.PositiveSmallIntegerField(default=0)

    objects = TeacherManager



    # post_save.connect(set_teacher_permission_group, sender=TeacherProfile)

# def create_profile(sender, instance, created, **kwargs):
#
#     if created:
#         print(instance.email, kwargs)
#
# def create_teacher_profile(sender, instance, created, **kwargs):
#     if created:
#         TeacherProfile.objects.create(user=instance)
#
# post_save.connect(create_profile, sender=User)


class StudentProfile(BaseProfile):

    lessons_taken = models.PositiveSmallIntegerField(default=0)


class LessonCreator(models.Model):

    teacher = models.OneToOneField(TeacherProfile)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # lessons_created = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.teacher.get_name_or_username()


@receiver(post_save, sender=TeacherProfile)
def set_teacher_permission_group(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        group = Group.objects.get(name='Teacher')
        group.user_set.add(user)

@receiver(post_save, sender=StudentProfile)
def set_student_permission_group(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        group = Group.objects.get(name='Student')
        group.user_set.add(user)