from rest_framework import serializers
from website.models import Temperature


class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperature
        fields = ['date', 'temperature']