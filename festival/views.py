from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from festival import models


class Index(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["username"] = self.request.user.username
        return context


class RequestView(PermissionRequiredMixin, CreateView):
    permission_required = ('festival.view_request')
    model = models.Request
    template_name = 'request.html'
    success_url = '/'
    fields = ['name', 'text', 'format', 'desired_scene', 'comment']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["username"] = self.request.user.username
        return context
