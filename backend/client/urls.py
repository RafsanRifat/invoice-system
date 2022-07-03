from django.urls import path
from .views import client, item_list, client_detail, client_invoice, invoice_detail, item_detail

urlpatterns = [
    path('api/clients', client, name="client"),
    path('api/items', item_list, name="items"),
    path('api/item/<int:item_id>', item_detail, name="item_detail"),
    path('api/invoice/<int:client_id>', client_invoice, name="invoice"),
    path('api/invoice_detail/<int:invoice_id>', invoice_detail, name="invoice_detail"),
    path('api/clients/<int:pk>', client_detail, name="client_detail")
]

# Endpoints list ----->>>

"""

Clients list        ------------->>>   http://localhost:8000/api/clients
Items list          ------------->>>   http://localhost:8000/api/items
Items Detail        ------------->>>   http://localhost:8000/api/item/<item_id>
Client Invoice list ------------->>>   http://localhost:8000/api/invoice/<Client_id>
Invoice Detail      ------------->>>   http://localhost:8000/api/invoice_detail/<invoice_id>
Client Detail       ------------->>>   http://localhost:8000/api/clients/<Client_id>

"""
