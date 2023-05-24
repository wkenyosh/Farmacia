from rest_framework import serializers
from farmacia_popular import models

class Farmacia_popularSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Farmacia_popular
        fields = '__all__'