from django.contrib import admin
from django.urls import path, include
from ledger.api.router import router_create, router_ledger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(router_create.urls)),
    path('transaction/', include(router_ledger.urls)),
    # path('accounts/create', include('ledger.api.router')),
    # path('transaction/', include('ledger.api.router')),
]
