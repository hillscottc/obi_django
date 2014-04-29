from django.conf.urls import patterns, url
import views


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),


    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^purchases/$', views.PurchaseList.as_view(), name='purchase-list'),

    url(r'^customers/(?P<pk>\d+)/$', views.CustomerDetail.as_view(), name='customer-detail'),
    url(r'^customers/$', views.CustomerList.as_view(), name='customer-list'),


    url(r'purchase/add/$', views.PurchaseCreate.as_view(), name='purchase-add'),




    url(r'purchase/(?P<pk>\d+)/delete/$', views.PurchaseDelete.as_view(), name='purchase-delete'),
)
