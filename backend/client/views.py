from django.shortcuts import render
from .models import Clients, Invoices, Items
from .serializers import Clientsserializer, ItemsSerializer, InvoiceSerilizer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def client_list(request):
    clients = Clients.objects.all()
    clients = Clientsserializer(clients, many=True)
    return Response(clients.data)


@api_view(['GET'])
def item_list(request):
    items = Items.objects.all()
    items = ItemsSerializer(items, many=True)
    return Response(items.data)


@api_view(['GET'])
def invoice_list(request):
    invoices = Invoices.objects.all()
    invoices = InvoiceSerilizer(invoices, many=True)
    return Response(invoices.data)
