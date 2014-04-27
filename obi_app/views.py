from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Purchase, Customer


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['customer', 'product']

    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user
    #     return super(PurchaseCreate, self).form_valid(form)


class PurchaseDelete(DeleteView):
    model = Purchase
    success_url = reverse_lazy('purchase-list')


class PurchaseList(ListView):
    model = Purchase


# class CustomerPurchaseList(ListView):
#
#     template_name = 'purchases/purchases_by_customer.html'
#
#     def get_queryset(self):
#         self.customer = get_object_or_404(Customer, name=self.args[0])
#         return Purchase.objects.filter(customer=self.customer)
#
#     def get_context_data(self, **kwargs):
#         context = super(CustomerPurchaseList, self).get_context_data(**kwargs)
#         context['customer'] = self.customer
#         return context


class CustomerDetail(SingleObjectMixin, ListView):
    """Customer and purchases."""
    paginate_by = 2
    template_name = "customers/customer_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Customer.objects.all())
        return super(CustomerDetail, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CustomerDetail, self).get_context_data(**kwargs)
        context['customer'] = self.object
        return context

    def get_queryset(self):
        return self.object.purchase_set.all()