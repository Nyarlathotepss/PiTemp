from website.models import Temperature
from rest_framework import viewsets
from api.serializers import TemperatureSerializer


class TemperatureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Temperature.objects.all().order_by('date')
    serializer_class = TemperatureSerializer

