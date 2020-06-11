from website.models import Temperature
from rest_framework import viewsets
from api.serializers import TemperatureSerializer
from rest_framework.permissions import IsAuthenticated   # <-- authentication api (1/2)


class TemperatureViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)   # <-- authentication api (2/2)
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Temperature.objects.all().order_by('date')
    serializer_class = TemperatureSerializer

