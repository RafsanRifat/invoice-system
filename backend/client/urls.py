from django.urls import path
from .views import client, item_list, client_detail, client_invoice, invoice_detail


urlpatterns = [
    path('api/clients', client, name="client"),
    path('api/items', item_list, name="items"),
    path('api/invoice/<int:client_id>', client_invoice, name="invoice"),
    path('api/invoice_detail/<int:invoice_id>', invoice_detail, name="invoice_detail"),
    path('api/clients/<int:pk>', client_detail, name="client_detail")
]
