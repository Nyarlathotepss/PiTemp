from website.models import Temperature
from rest_framework import viewsets
from api.serializers import TemperatureSerializer
from rest_framework.authentication import TokenAuthentication   # <-- authentication api (1/4)
from rest_framework.permissions import IsAuthenticated   # <-- authentication api (2/4)


class TemperatureViewSet(viewsets.ModelViewSet):

    authentication_classes = [TokenAuthentication]   # <-- authentication api (3/4)
    permission_classes = [IsAuthenticated]   # <-- authentication api (4/4)

    """
    API endpoint that allows temperature to be viewed or edited.
    """
    queryset = Temperature.objects.all().order_by('date')
    serializer_class = TemperatureSerializer

    def perform_create(self, serializer):    # insert idUser in POST request
        serializer.save(idUser=self.request.user)
