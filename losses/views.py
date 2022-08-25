from rest_framework import generics

from .models import Loss
from .serializers import LossSerializer


class ListCreateLossView(generics.ListCreateAPIView):
    queryset = Loss.objects.all()
    serializer_class = LossSerializer


class RetrieveUpdateDestroyLossView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loss.objects.all()
    serializer_class = LossSerializer

    lookup_url_kwarg = "loss_id"
