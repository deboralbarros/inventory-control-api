from django.urls import path

from .views import ListCreateProductView, RetrieveUpdateDestroyProductView

urlpatterns = [
    path('products/', ListCreateProductView.as_view()),
    path('products/<str:pk>/', RetrieveUpdateDestroyProductView.as_view())
]
