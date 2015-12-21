from django.conf.urls import url, include
from rest_framework import routers
from . import views



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

router = routers.DefaultRouter()
router.register(r'currency', views.CurrencyViewSet)
router.register(r'exchange', views.ExchangeViewSet)

urlpatterns = [
     url(r'^', include(router.urls)),

]