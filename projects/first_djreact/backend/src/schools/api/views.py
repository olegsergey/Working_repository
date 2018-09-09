from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)

from schools.models import School
from .serializers import SchoolSerializer


class SchoolListView(ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class SchoolDetailView(RetrieveAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class SchoolCreateView(CreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class SchoolUpdateView(UpdateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class SchoolDeleteView(DestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer