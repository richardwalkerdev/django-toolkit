from django.urls import path
from .views import MonitoringPageView

urlpatterns = [
    path('custom', MonitoringPageView.as_view(), name='monitoring'),
]
