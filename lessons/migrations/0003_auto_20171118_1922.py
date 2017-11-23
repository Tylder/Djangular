# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-18 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_creator', '0002_auto_20171118_1922'),
        ('lessons', '0002_lesson_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonpart',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lessonpart',
            name='approved_by',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='approved_by', to='lesson_creator.LessonCreator'),
        ),
        migrations.AddField(
            model_name='lessonpart',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lessonpart',
            name='created_by',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='lesson_creator.LessonCreator'),
        ),
        migrations.AddField(
            model_name='lessonpart',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='lessonpart',
            name='updated_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by', to='lesson_creator.LessonCreator'),
        ),
    ]
