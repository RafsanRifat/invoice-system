from django.shortcuts import render
from .models import Clients, Invoices, Items
from .serializers import Clientsserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def client_list(request):
    clients = Clients.objects.all()
    clients = Clientsserializer(clients, many=True)
    return Response(clients.data)



