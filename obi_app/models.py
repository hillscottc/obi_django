from django.db import models
from django.forms import ModelForm
from django.core.urlresolvers import reverse


class Customer(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=35, blank=True, null=True)
    company = models.CharField(max_length=35, blank=True, null=True)
    email = models.EmailField(max_length=40, blank=True, null=True, unique=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    notes = models.CharField(max_length=80, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('customer-detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return "{} {}".format(self.fname, self.lname)


class Product(models.Model):
    code = models.CharField(max_length=4, blank=True, null=True, unique=True)
    name = models.CharField(max_length=35)
    is_active = models.BooleanField(default=True)
    desc = models.CharField(max_length=80)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.code


class Purchase(models.Model):
    customer = models.ForeignKey(Customer)
    product = models.ForeignKey(Product)
    timestamp = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('purchase-detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return "{}, {}, {}".format(self.customer, self.product, self.timestamp)


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ['customer', 'product']