from django.urls import path
from .views import (
    SupplierListCreateAPIView,
    SupplierRetrieveUpdateAPIVIew
)


urlpatterns = [
    path(
        '',
        SupplierListCreateAPIView.as_view(), 
        name='suppliers-list-create-api-view'
    ),
    path(
        '<str:id>/',
        SupplierRetrieveUpdateAPIVIew.as_view(),
        name='suppliers-retrieve-update-destroy-api-view'
    )
]
