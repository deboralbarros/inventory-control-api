from django.urls import path

from .views import ListCreateMovementView


urlpatterns = [
    path('', ListCreateMovementView.as_view())
]
