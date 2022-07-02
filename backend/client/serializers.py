from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Clients, Invoices, Items


class Clientsserializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'
