"""Serializer is used to translate the Django models from python to JSON"""


from rest_framework import serializers

from .models import *


class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TeacherProfile
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentProfile
        fields = '__all__'


# class ListSerializer(serializers.ModelSerializer):
#     user = CardSerializer(read_only=True, many=True) # to show the cards as a property of Lists
#
#     class Meta:
#         model = List #This is the model that will get serialized
#         fields = '__all__'
#


