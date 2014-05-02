from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required
import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),


    # url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^$', login_required(views.home_redirect), name='home'),



    url(r'^purchases/$', login_required(views.PurchaseList.as_view()), name='purchase-list'),

    url(r'^customers/(?P<pk>\d+)/$', login_required(views.CustomerDetail.as_view()), name='customer-detail'),
    url(r'^customers/$', login_required(views.CustomerList.as_view()), name='customer-list'),


    url(r'purchase/add/$', login_required(views.PurchaseCreate.as_view()), name='purchase-add'),




    url(r'purchase/(?P<pk>\d+)/delete/$', login_required(views.PurchaseDelete.as_view()), name='purchase-delete'),
)
