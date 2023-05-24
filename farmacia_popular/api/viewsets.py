from rest_framework import viewsets
from farmacia_popular.api import serializers
from farmacia_popular import models


class Farmacia_popularViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.Farmacia_popularSerializer
    queryset = models.Farmacia_popular.objects.all()
    
