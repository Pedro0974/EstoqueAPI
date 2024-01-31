from django.urls import path
from .views import (
    ProductListCreateAPIView,
    ProductRetrieveUpdateAPIView
)


urlpatterns = [
    path(
        '',
        ProductListCreateAPIView.as_view(), 
        name='products-list-create-api-view'
    ),
    path(
        '<str:id>/',
        ProductRetrieveUpdateAPIView.as_view(),
        name='products-retrieve-update-destroy-api-view'
    )
]
