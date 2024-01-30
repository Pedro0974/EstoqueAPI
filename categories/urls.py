from django.urls import path
from .views import (
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateAPIView
)


urlpatterns = [
    path(
        '',
        CategoryListCreateAPIView.as_view(), 
        name='categories-list-create-api-view'
    ),
    path(
        '<str:id>/',
        CategoryRetrieveUpdateAPIView.as_view(),
        name='categories-retrieve-update-destroy-api-view'
    )
]
