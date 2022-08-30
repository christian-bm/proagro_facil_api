import datetime

from geopy.distance import distance
from rest_framework import generics, views

from .models import Loss
from .serializers import LossSerializer


class ListCreateLossView(generics.ListCreateAPIView):
    queryset = Loss.objects.all()
    serializer_class = LossSerializer

    def get_queryset(self):
        losses = Loss.objects.all()

        return losses.order_by("create_at").reverse()

    def post(self, request, *args, **kwargs):
        data = request.data
        losses = Loss.objects.all()
        filtedLosses = losses.filter(cpf=data["cpf"])
        filtedLosses = filtedLosses.filter(harvest_date=data["harvest_date"])

        for loss in filtedLosses:
            if (
                distance(
                    (data["latitude"], data["longitude"]),
                    (loss.latitude, loss.longitude),
                ).km
                <= 10
            ):
                if loss.event_type != data["event_type"]:
                    return views.Response(status=views.status.HTTP_409_CONFLICT)

        serializer = LossSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return views.Response(serializer.data, views.status.HTTP_201_CREATED)


class RetrieveUpdateDestroyLossView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loss.objects.all()
    serializer_class = LossSerializer

    lookup_url_kwarg = "loss_id"


class ListCpfLossView(generics.ListAPIView):
    queryset = Loss.objects.all()
    serializer_class = LossSerializer

    def get_queryset(self):
        return Loss.objects.filter(cpf=self.kwargs["cpf"])


# class VerifyLossView(views.APIView):
#     def post(self, request):
#         data = request.data
#         print(data)
#         losses = Loss.objects.all()

#         # lossesFilt = losses.filter(harvest_date=date)

#         # result = []

#         # for loss in lossesFilt:
#         #     if distance((lat, lon), (loss.latitude, loss.longitude)).km <= 10:
#         #         if loss.event_type == event:
#         #             result.append(loss)

#         # if len(result) != 0:
#         #     return views.Response(status=views.status.HTTP_409_CONFLICT)

#         return views.Response(status=views.status.HTTP_200_OK)
