from rest_framework.routers import DefaultRouter
from ledger.api.views import AccountModelViewSet, LedgerModelViewSet

router_create = DefaultRouter()
router_ledger = DefaultRouter()

router_create.register(prefix='create', basename='create', viewset=AccountModelViewSet)
router_ledger.register(prefix='ledger', basename='ledger', viewset=LedgerModelViewSet)
