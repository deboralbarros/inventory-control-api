from django.urls import path

from .views import ListCreateProductView

urlpatterns = [
    path('products/', ListCreateProductView.as_view())
]
