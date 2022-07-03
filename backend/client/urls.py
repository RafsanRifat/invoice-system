from django.urls import path
from .views import client, item_list, invoice_list, client_detail, client_invoice


urlpatterns = [
    path('api/clients', client, name="client"),
    path('api/items', item_list, name="items"),
    path('api/invoices', invoice_list, name="invoices"),
    path('api/invoice/<int:pk>', client_invoice, name="invoice"),
    path('api/clients/<int:pk>', client_detail, name="client_detail")
]
