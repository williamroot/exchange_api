from .serializers import CurrencySerialiazer, ExchangeSerialiazer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Currency, Exchange

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerialiazer


class ExchangeViewSet(viewsets.ModelViewSet):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerialiazer

    def get(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
