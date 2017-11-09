"""Serializer is used to translate the Django models from python to JSON"""


from rest_framework import serializers

from .models import List, Card


class CardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Card
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):
    cards = CardSerializer(read_only=True, many=True) # to show the cards as a property of Lists

    class Meta:
        model = List #This is the model that will get serialized
        fields = '__all__'



