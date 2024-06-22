from django.urls import path

from apps.views import DashboardView, ContactView, SignForNewsCreateView,PartnersView

urlpatterns = [
    path('', DashboardView.as_view(), name='base_dashboard_view'),
    path('contacts/', ContactView.as_view(), name='contact_view'),
    path('sign/', SignForNewsCreateView.as_view(), name='sign_for_news_view'),
    path('partners/', PartnersView.as_view(), name='partners_view')
]
