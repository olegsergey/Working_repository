from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)

from schooldatas.models import Schooldata
from .serializers import SchooldataSerializer


class SchooldataListView(ListAPIView):
    queryset = Schooldata.objects.all()
    serializer_class = SchooldataSerializer


class SchooldataDetailView(RetrieveAPIView):
    queryset = Schooldata.objects.all()
    serializer_class = SchooldataSerializer

class SchooldataCreateView(CreateAPIView):
    queryset = Schooldata.objects.all()
    serializer_class = SchooldataSerializer


class SchooldataUpdateView(UpdateAPIView):
    queryset = Schooldata.objects.all()
    serializer_class = SchooldataSerializer


class SchooldataDeleteView(DestroyAPIView):
    queryset = Schooldata.objects.all()
    serializer_class = SchooldataSerializer