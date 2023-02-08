from rest_framework.serializers import ModelSerializer
from ledger.models.account_model import AccountModel
from ledger.models.ledger_model import LedgerModel

class AccountSerializer(ModelSerializer):

    class Meta:
        model = AccountModel
        fields = ['client_id', 'account_type', 'amount']

class LedgerSerializer(ModelSerializer):

    class Meta:
        model = LedgerModel
        fields = ['client_id', 'ledger_type', 'amount', 'description']
