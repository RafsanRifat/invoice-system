from django.urls import path
from .views import client_list, item_list, invoice_list


urlpatterns = [
    path('api/clients', client_list, name="client_list"),
    path('api/items', item_list, name="items"),
    path('api/invoices', invoice_list, name="invoices")
]
