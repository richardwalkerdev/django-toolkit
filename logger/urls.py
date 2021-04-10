from django.urls import path
from .views import LoggerPageView

urlpatterns = [
    path('logger', LoggerPageView.as_view(), name='logger'),
]
