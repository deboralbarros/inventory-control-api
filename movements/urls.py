from django.urls import path

from .views import ListCreateMovementView


urlpatterns = [
    path('movements/', ListCreateMovementView.as_view())
]
