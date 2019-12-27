from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


from users.models import UserProfile
from festival import models, forms


class Index(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["username"] = self.request.user.username
        return context


class ManageRequests(ListView):
    template_name = 'manage-requests.html'
    model = models.Voice

    def dispatch(self, request, *args, **kwargs):  
        if self.request.user.is_anonymous:  
            return HttpResponseRedirect(reverse_lazy('users:login'))  
        if not self.request.user.has_perm('festival.change_request'):
            return HttpResponseRedirect(reverse_lazy('festival:request'))
        return super(ManageRequests, self).dispatch(request, *args, **kwargs)  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context


class RequestView(CreateView):
    model = models.Request
    template_name = 'request.html'
    success_url = '/'
    fields = ['name', 'text', 'format', 'desired_scene', 'comment']

    def dispatch(self, request, *args, **kwargs):  
        if self.request.user.is_anonymous:  
            return HttpResponseRedirect(reverse_lazy('users:login'))  
        r = models.Request.objects.filter(owner=UserProfile.objects.filter(user=self.request.user).first()).first()
        if r:
            return HttpResponseRedirect(reverse_lazy('festival:request_status', args=[r.id]))
        return super(RequestView, self).dispatch(request, *args, **kwargs)  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["username"] = self.request.user.username
        return context

    def form_valid(self, form):  
        instance = form.save(commit=False)  
        instance.owner = UserProfile.objects.get(user=self.request.user)  
        instance.save()  
        return super(RequestView, self).form_valid(form)


class RequestStatus(PermissionRequiredMixin, DetailView):
    model = models.Request
    template_name = 'request-status.html'


    def has_permission(self):
        r = models.Request.objects.values('id').filter(owner=UserProfile.objects.get(user=self.request.user)).first()
        if r['id'] == self.kwargs['pk']:
            return True
        return False

    def dispatch(self, request, *args, **kwargs):  
        if self.request.user.is_anonymous:  
            return HttpResponseRedirect(reverse_lazy('users:login'))  
        return super(RequestStatus, self).dispatch(request, *args, **kwargs)  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["username"] = self.request.user.username
        return context

class VoteView(FormView):
    template_name = 'voice-form.html'
    model = models.Voice
    form_class = forms.VoteForm

    def get_context_data(self, **kwargs):

# TODO Разрешить только цензорам

        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["username"] = self.request.user.username
            context["ID"] = self.kwargs['request_id']
        return context