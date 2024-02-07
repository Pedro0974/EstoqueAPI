from django.urls import path
from .views import (
    ProhibitedListCreateAPIView,
    ProhibitedRetrieveUpdateAPIView,
    ExitListCreateAPIView,
    ExitRetrieveUpdateAPIView
)


urlpatterns = [
    path(
        '',
        ProhibitedListCreateAPIView.as_view(), 
        name='prohibited-list-create-api-view'
    ),
    path(
        '<str:id>/',
        ProhibitedRetrieveUpdateAPIView.as_view(),
        name='prohibited-retrieve-update-destroy-api-view'
    ),
    path(
        '',
        ExitListCreateAPIView.as_view(), 
        name='exit-list-create-api-view'
    ),
    path(
        '<str:id>/',
        ExitRetrieveUpdateAPIView.as_view(),
        name='exit-retrieve-update-destroy-api-view'
    ),
]
