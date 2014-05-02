import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import (HttpResponse, RequestContext, redirect,
                              render_to_response, HttpResponseRedirect)
from django.core.urlresolvers import reverse
from django.views.generic import ListView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.conf import settings
from .models import Purchase, Customer
from postmark import PMMail
import logging

logger = logging.getLogger('testlogger')


def send_reward_email(**kwargs):
    message = PMMail(api_key=os.environ.get('POSTMARK_API_KEY'),
                     subject="Your reward from Obi",
                     sender="shill@taluslabs.com",
                     **kwargs)
    message.send()


# class HomePageView(TemplateView):
#     template_name = "home.html"
#     def get_context_data(self, **kwargs):
#         context = super(HomePageView, self).get_context_data(**kwargs)
#         # context['latest_articles'] = Article.objects.all()[:5]
#         return context


def home_redirect(request):
    return redirect('purchase-add')


class PurchaseCreate(SuccessMessageMixin, CreateView):
    template_name = "purchase_form.html"

    model = Purchase
    fields = ['customer', 'product']
    success_url = reverse_lazy('purchase-list')
    # success_message = "It was created successfully"

    def form_valid(self, form):
        customer = form.cleaned_data['customer']
        product = form.cleaned_data['product']
        count = Purchase.objects.filter(customer=customer).count() + 1

        msg = "Purchase number %d for %s. " % (count, customer)

        if count % settings.REWARD_MULTIPLE == 0:
            if customer.email:
                send_reward_email(
                    to=customer.email,
                    text_body="".join(["Congratulations on purchase number %d from Obi's!" % count,
                                       "To show our thanks, come on in for a FREE order. See you soon!"]))
                msg += "Reward email sent."
            else:
                msg += "Earned a reward, but no email on record for this customer."

        messages.add_message(self.request, messages.INFO, msg)
        return super(PurchaseCreate, self).form_valid(form)


class PurchaseList(ListView):
    model = Purchase
    template_name = "purchase_list.html"


class CustomerList(ListView):
    model = Customer
    template_name = "customer_list.html"


class CustomerDetail(SingleObjectMixin, ListView):
    """Customer and purchases."""
    paginate_by = 50
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


def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('quiz_index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('login.html', {}, context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')



