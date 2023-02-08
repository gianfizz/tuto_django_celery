from ledger.models.ledger_model import LedgerModel, LedgerType
from django.core.exceptions import ValidationError

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from celery import shared_task

@shared_task()
@receiver(post_save, sender=LedgerModel)
def ledger_model_post_save(sender, created ,instance: LedgerModel, **kwargs):
    if created:
        if instance.ledger_type == LedgerType.IN.value:
            instance.client_id.amount += instance.amount
        if instance.ledger_type == LedgerType.OUT.value:
            instance.client_id.amount -= instance.amount
        instance.client_id.save()

@shared_task()
@receiver(pre_save, sender=LedgerModel)
def ledger_model_pre_save(sender, instance: LedgerModel, **kwargs):
    if instance.ledger_type == LedgerType.OUT.value:
        if (instance.client_id.amount - instance.amount) < 0:
            raise ValidationError('Invalid Amount')
