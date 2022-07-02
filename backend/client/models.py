from django.db import models


# Create your models here.

class Clients(models.Model):
    Choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    client_name = models.CharField(max_length=200)
    client_company_name = models.CharField(max_length=220)
    client_phone = models.CharField(max_length=20)
    client_email = models.EmailField()
    clint_address = models.CharField(max_length=220)
    client_city = models.CharField(max_length=220, null=True, blank=True)
    client_state = models.CharField(max_length=220, null=True, blank=True)
    client_zip = models.CharField(max_length=50, null=True, blank=True)
    client_image = models.ImageField(blank=True, null=True, upload_to='images/')
    client_birthdate = models.DateTimeField(blank=True, null=True)
    client_gender = models.CharField(null=True, blank=True, max_length=50, choices=Choices)


    class Meta:
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.client_name


class Invoices(models.Model):
    clients = models.ForeignKey(Clients, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True)
    pdffile = models.FileField(upload_to='pdf/', null=True, blank=True)

    @property
    def total(self):
        price = 0
        for item in self.items_set.all():
            tprice = item.total_price
            price = price + tprice
        return price

    class Meta:
        verbose_name_plural = 'Invoices'

    def combined(self):
        return f"  Invoice of {self.clients.client_name} At {self.date}"

    def __str__(self):
        return self.combined()


class Items(models.Model):
    invoice = models.ForeignKey(Invoices, on_delete=models.CASCADE)
    name = models.CharField(max_length=220, null=True, blank=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    # total_price = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Items'

    @property
    def total_price(self):
        return self.quantity * self.price

    # def __str__(self):
    #     return self.item_name

    def __str__(self):
        return str(self.total_price)
