from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Clients, Invoices, Items


class Clientsserializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'


class InvoiceSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Invoices
        fields = '__all__'
