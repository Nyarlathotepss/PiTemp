from website.models import Temperature
from rest_framework import viewsets
from api.serializers import TemperatureSerializer
from rest_framework.authentication import TokenAuthentication   # <-- authentication api (1/4)
from rest_framework.permissions import IsAuthenticated   # <-- authentication api (2/4)


class TemperatureViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Temperature.objects.all().order_by('date')
    serializer_class = TemperatureSerializer
    authentication_classes = (TokenAuthentication,)   # <-- authentication api (3/4)
    permission_classes = (IsAuthenticated,)   # <-- authentication api (4/4)
