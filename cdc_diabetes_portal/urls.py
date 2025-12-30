"""URL configuration for cdc_diabetes_portal project."""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('diabetes_api.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]
