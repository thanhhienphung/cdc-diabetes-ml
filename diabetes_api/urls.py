from django.urls import path

from .views import predict_view

urlpatterns = [
    path('diabetes-predict', predict_view, name='predict'),
]
