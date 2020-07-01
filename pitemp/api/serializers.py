from rest_framework import serializers
from website.models import Temperature


class TemperatureSerializer(serializers.ModelSerializer):
    idUser = serializers.PrimaryKeyRelatedField(read_only=True)    # Insert idUser in POST request

    class Meta:
        model = Temperature
        fields = ['date', 'temperature', 'idUser']
