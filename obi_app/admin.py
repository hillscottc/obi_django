from django.contrib import admin

from obi_app.models import Customer, Product, Purchase

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Purchase)