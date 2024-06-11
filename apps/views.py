from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from apps.forms import EmailForm


class DashboardView(TemplateView):
    template_name = 'apps/dashboard.html'


class ContactView(TemplateView):
    template_name = 'apps/contact.html'


class SignForNewsCreateView(CreateView):
    template_name = 'apps/dashboard.html'
    form_class = EmailForm
    success_url = reverse_lazy('base_dashboard_view')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('.', {'form': form})
