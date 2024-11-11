from django.views.generic import TemplateView

class RSCView(TemplateView):
    template_name = 'auth/rsc.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Answer Page'
        return context