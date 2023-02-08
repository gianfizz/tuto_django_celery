from django.db import models
import uuid
from ledger.models.account_model import AccountModel
from django.core.exceptions import ValidationError

class LedgerType(models.Choices):
    IN = "IN"
    OUT = "OUT"

class MinMaxFloat(models.FloatField):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        super(MinMaxFloat, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(MinMaxFloat, self).formfield(**defaults)

class LedgerModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    client_id = models.ForeignKey(AccountModel, on_delete=models.DO_NOTHING)
    ledger_type = models.CharField(max_length=3, choices=LedgerType.choices)
    amount = MinMaxFloat(min_value=0.0)
    description = models.TextField(default="No Description", blank=True)

    def __str__(self):
        return f"{self.client_id}, type: {self.ledger_type}, amount: {self.amount}"
