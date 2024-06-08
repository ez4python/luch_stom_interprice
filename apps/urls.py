from django.urls import path

from apps.views import DashboardView, ContactView

urlpatterns = [
    path('', DashboardView.as_view(), name='base_dashboard_view'),
    path('contacts/', ContactView.as_view(), name='contact_view'),
]
