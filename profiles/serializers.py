"""Serializer is used to translate the Django models from python to JSON"""
from django.http import JsonResponse
from rest_framework import serializers

from .models import *




class TeacherSerializer(serializers.ModelSerializer):

    # # Create a custom method field
    # current_user = serializers.SerializerMethodField('_user')
    #
    # # Use this method for the custom field
    # def _user(self, obj):
    #     user = self.context['request'].user.id
    #     print(user)
    #     return JsonResponse({"models_to_return": user})

    class Meta:
        model = TeacherProfile
        fields = '__all__'
        read_only_fields = ('user',)


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentProfile
        fields = '__all__'
        read_only_fields = ('user',)


class LessonCreatorSerializer(serializers.ModelSerializer):
        class Meta:
            model = LessonCreator
            fields = '__all__'
# class ListSerializer(serializers.ModelSerializer):
#     user = CardSerializer(read_only=True, many=True) # to show the cards as a property of Lists
#
#     class Meta:
#         model = List #This is the model that will get serialized
#         fields = '__all__'
#


