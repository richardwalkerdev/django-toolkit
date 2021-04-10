from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('', include('monitoring.urls')),
    path('', include('logger.urls')),
    path('', include('django_prometheus.urls')),
]
