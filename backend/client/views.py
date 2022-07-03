from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser

from .models import Clients, Invoices, Items
from .serializers import Clientsserializer, ItemsSerializer, InvoiceSerilizer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Client List and create client
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


# Client Detail, Update And Delete
@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, pk):
    client = Clients.objects.get(id=pk)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serilizer = Clientsserializer(client, data=data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({"Message": "You have successfully updated the client"})
        else:
            return Response({"Message": "Somethins"})
    elif request.method == 'DELETE':
        client.delete()
        return Response({"Message": "The client has deleted"})
    client = Clients.objects.get(id=pk)
    client = Clientsserializer(client)

    return Response(client.data)


# Client invoice
@api_view(['GET', 'POST'])
def client_invoice(request, client_id):
    if request.method == 'POST':
        serilizer = InvoiceSerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response({"message": "Something went wrong"})
    client = Clients.objects.get(id=client_id)
    invoice = client.invoices_set.all()
    serilizer = InvoiceSerilizer(invoice, many=True)
    return Response(serilizer.data)


# Invoice detail, edit, delete
@api_view(['GET', 'Put', 'DELETE'])
def invoice_detail(request, invoice_id):
    invoice = Invoices.objects.get(id=invoice_id)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serilizer = InvoiceSerilizer(invoice, data=data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({"": "Successfully updated"})
        else:
            return Response({"message": "Something went wrong"})
    elif request.method == 'DELETE':
        invoice.delete()
        return Response({"Message": "Item Deleted Successfully"})
    invoice = Invoices.objects.get(id=invoice_id)
    invoice_detail = InvoiceSerilizer(invoice)
    return Response(invoice_detail.data)


# Item list and create Items
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
