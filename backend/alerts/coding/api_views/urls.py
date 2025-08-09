from django.urls import path, include
from .authentication import urls as urls_authentication
from .stocks import urls as urls_stocks
from .alerts import urls as urls_alerts
from .triggered import urls as urls_triggered


urlpatterns = [
    path('auth/', include(urls_authentication)),
    path('stocks/', include(urls_stocks)),
    path('alerts/', include(urls_alerts)),
    path('triggered/', include(urls_triggered)),
]
