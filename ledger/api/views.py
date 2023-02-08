from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from ledger.models.account_model import AccountModel
from ledger.models.ledger_model import LedgerModel
from ledger.api.serializers import AccountSerializer, LedgerSerializer

class AccountModelViewSet(ModelViewSet):
    serializer_class = AccountSerializer
    queryset = AccountModel.objects.all()

class LedgerModelViewSet(ModelViewSet):
    serializer_class = LedgerSerializer
    queryset = LedgerModel.objects.all()
