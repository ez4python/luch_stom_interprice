from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = 'apps/dashboard.html'


class ContactView(TemplateView):
    template_name = 'apps/contact.html'
