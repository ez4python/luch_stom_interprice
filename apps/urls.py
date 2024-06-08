from django.urls import path

from apps.views import DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='base_dashboard_view'),
]
