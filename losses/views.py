from rest_framework import generics

from .models import Loss
from .serializers import LossSerializer


class ListCreateLossView(generics.ListCreateAPIView):
    queryset = Loss.objects.all()
    serializer_class = LossSerializer

    def get_queryset(self):
        losses = Loss.objects.all()

        return losses.order_by("create_at").reverse()


class RetrieveUpdateDestroyLossView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loss.objects.all()
    serializer_class = LossSerializer

    lookup_url_kwarg = "loss_id"


class ListCpfLossView(generics.ListAPIView):
    queryset = Loss.objects.all()
    serializer_class = LossSerializer

    def get_queryset(self):
        return Loss.objects.filter(cpf=self.kwargs["cpf"])
