from django.views.generic.base import TemplateView


class Index(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["username"] = self.request.user.username
        context["my_var"] = "my value"
        return context
