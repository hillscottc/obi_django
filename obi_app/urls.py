from django.conf.urls import patterns, url
from .views import PurchaseCreate, PurchaseDelete, CustomerDetail

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # url(r'^purchase/$', PublisherList.as_view(), name='purchase_list'),

    url(r'^customers/(?P<pk>\d+)/$', CustomerDetail.as_view(), name='customer-detail'),

    url(r'purchase/add/$', PurchaseCreate.as_view(), name='purchase_add'),
    url(r'purchase/(?P<pk>\d+)/delete/$', PurchaseDelete.as_view(), name='purchase_delete'),
)
