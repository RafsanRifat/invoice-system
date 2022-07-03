from django.shortcuts import render
from .models import Clients, Invoices, Items
from .serializers import Clientsserializer, ItemsSerializer, InvoiceSerilizer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET', 'POST'])
def client(request):
    if request.method == 'POST':
        serilizer = Clientsserializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
        else:
            return Response({"Message": "Something went wrong"})
    clients = Clients.objects.all()
    clients = Clientsserializer(clients, many=True)
    return Response(clients.data)


@api_view(['GET', 'POST'])
def item_list(request):
    if request.method == 'POST':
        serilizer = ItemsSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
        else:
            return Response({"Message": "Something went wrong"})
    items = Items.objects.all()
    items = ItemsSerializer(items, many=True)
    return Response(items.data)


@api_view(['GET', 'POST'])
def invoice_list(request):
    if request.method == 'POST':
        serilizer = InvoiceSerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
        else:
            return Response({"Message": "Something went wrong"})
    invoices = Invoices.objects.all()
    invoices = InvoiceSerilizer(invoices, many=True)
    return Response(invoices.data)


@api_view(['GET', 'POST'])
def client_detail(request, pk):
    client = Clients.objects.get(id=pk)
    print(client)
    client = Clientsserializer(client)

    return Response(client.data)
