from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, FormView, DetailView

from apps.forms import EmailForm, ContactForm
from apps.models import Product, NewsReceiver, Category
from apps.tasks import task_contact_with
from root.settings import DEFAULT_RECIPIENT


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
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['email']
        recipient = [DEFAULT_RECIPIENT]
        message = f"Name: {name}\n\nFrom-email: {sender}\n\nPhone: {phone}\n\nMessage:\n{message}"
        task_contact_with.delay(subject, message, recipient)
        if not NewsReceiver.objects.filter(email=sender).exists():
            NewsReceiver.objects.create(email=sender)
        return super().form_valid(form)


class ProductsListView(ListView):
    template_name = 'apps/products_list.html'
    queryset = Product.objects.order_by('-id')
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.request.GET.get('category')
        queryset = super().get_queryset()
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['all_products_amount'] = Product.objects.count()
        context['is_all_categories'] = True
        context['categories'] = [
            {
                'pk': category.pk,
                'name': category.name,
                'amount': category.count_product()
            } for category in Category.objects.all()
        ]
        return context
class ProductDetailView(TemplateView):
    template_name = 'apps/product_detail.html'
