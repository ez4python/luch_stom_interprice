from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, FormView
from root.settings import DEFAULT_RECIPIENT

from apps.forms import EmailForm, ContactForm
from apps.models import Product


class DashboardView(ListView):
    template_name = 'apps/dashboard.html'
    queryset = Product.objects.order_by('-id')


class ContactView(TemplateView):
    template_name = 'apps/contact.html'


class PartnersView(TemplateView):
    template_name = 'apps/partners.html'
    queryset = Product.objects.order_by('-id')


class SignForNewsCreateView(CreateView):
    template_name = 'apps/dashboard.html'
    form_class = EmailForm
    success_url = reverse_lazy('base_dashboard_view')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('.', {'form': form})


class ContactFormView(FormView):
    template_name = 'apps/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_view')

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['email']
        recipient = [DEFAULT_RECIPIENT]
        message = f"Name: {form.cleaned_data['name']}\n\nPhone: {form.cleaned_data['phone']}\n\nMessage:\n{message}"
        send_mail(subject, message, sender, recipient)
        return super().form_valid(form)
