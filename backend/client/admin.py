from django.contrib import admin
from .models import Clients, Items, Invoices

# Register your models here.
admin.site.register(Clients)
admin.site.register(Items)
admin.site.register(Invoices)
