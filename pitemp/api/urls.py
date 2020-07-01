from django.urls import include, path
from rest_framework import routers
from api import views as my_view

router = routers.DefaultRouter()
router.register(r'temperatures', my_view.TemperatureViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]