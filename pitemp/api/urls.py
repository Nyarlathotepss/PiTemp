from django.urls import include, path
from rest_framework import routers
from api import views as my_view
from rest_framework.authtoken import views   # <-- authentication api (1/2)

router = routers.DefaultRouter()
router.register(r'temperatures', my_view.TemperatureViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),    # <-- authentication api (2/2)
]