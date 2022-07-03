from django.urls import path
from .views import client, item_list, invoice_list, client_detail


urlpatterns = [
    path('api/clients', client, name="client"),
    path('api/items', item_list, name="items"),
    path('api/invoices', invoice_list, name="invoices"),
    path('api/client_detail/<int:pk>', client_detail, name="client_detail")
]
