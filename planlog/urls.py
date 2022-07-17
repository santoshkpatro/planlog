from django.contrib import admin
from django.urls import path, include
from planlog.health import health_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('planlog.api.v1.urls')),
    path('api/health/', health_view)
]
