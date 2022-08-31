from rest_framework import serializers

from .models import Loss


class LossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loss
        fields = "__all__"
        read_only_fields = ["id"]
