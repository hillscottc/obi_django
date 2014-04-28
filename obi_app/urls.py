from django.conf.urls import patterns, url
import views


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^purchase/$', views.PurchaseList.as_view(), name='purchase_list'),

    url(r'^customers/(?P<pk>\d+)/$', views.CustomerDetail.as_view(), name='customer-detail'),

    url(r'purchase/add/$', views.PurchaseCreate.as_view(), name='purchase_add'),
    url(r'purchase/(?P<pk>\d+)/delete/$', views.PurchaseDelete.as_view(), name='purchase_delete'),
)
