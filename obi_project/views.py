from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control, never_cache
from django.views.generic import View


class NoCacheMixIn(View):
    # @method_decorator(cache_control(no_cache=True))
    # @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(NoCacheMixIn, self).dispatch(*args, **kwargs)


class LoginRequiredMixIn(NoCacheMixIn):
    # @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixIn, self).dispatch(*args, **kwargs)