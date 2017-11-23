"""Serving the JSON so that the client can retrieve it, this is the View
   A client makes a request on the site, Angular, frontend, will send a request to Django, backend,
   for that data.
   The views is what handles that request it will retrieve the appropriate data from the database
   and send it to the serializer to convert it to JSON and then return it to the client.
"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ListSerializer, CardSerializer
from .models import List, Card


class ListViewSet(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (AllowAny,)


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (AllowAny,)
    # permission_classes = (permissions.IsAuthenticated,)
