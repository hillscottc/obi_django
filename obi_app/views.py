from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Purchase, Customer


class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context


class PurchaseCreate(CreateView):
    template_name = "purchase_form.html"
    model = Purchase
    fields = ['customer', 'product']
    success_url = reverse_lazy('purchase-list')

    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user
    #     return super(PurchaseCreate, self).form_valid(form)


class PurchaseList(ListView):
    model = Purchase
    template_name = "purchase_list.html"


class CustomerList(ListView):
    model = Customer
    template_name = "customer_list.html"


class CustomerDetail(SingleObjectMixin, ListView):
    """Customer and purchases."""
    paginate_by = 3
    template_name = "customer_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Customer.objects.all())
        return super(CustomerDetail, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CustomerDetail, self).get_context_data(**kwargs)
        context['customer'] = self.object
        return context

    def get_queryset(self):
        return self.object.purchase_set.all()


class PurchaseDelete(DeleteView):
    model = Purchase
    success_url = reverse_lazy('purchase-list')



