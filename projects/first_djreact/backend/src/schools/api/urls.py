from django.urls import path

from .views import (
    SchoolListView, 
    SchoolCreateView, 
    SchoolDetailView,
    SchoolDeleteView,
    SchoolUpdateView
)

urlpatterns = [
    path('', SchoolListView.as_view()),
    path('create/', SchoolCreateView.as_view()),
    path('<pk>', SchoolDetailView.as_view()),
    path('<pk>/update/', SchoolUpdateView.as_view()),
    path('<pk>/delete/', SchoolDeleteView.as_view())
]

