from django.urls import path

from .views import (
    SchooldataListView, 
    SchooldataCreateView, 
    SchooldataDetailView,
    SchooldataDeleteView,
    SchooldataUpdateView
)

urlpatterns = [
    path('', SchooldataListView.as_view()),
    path('create/', SchooldataCreateView.as_view()),
    path('<pk>', SchooldataDetailView.as_view()),
    path('<pk>/update/', SchooldataUpdateView.as_view()),
    path('<pk>/delete/', SchooldataDeleteView.as_view())
]

