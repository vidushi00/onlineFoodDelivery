from rest_framework import serializers

from deliveryDetailApp.models import DeliveryDetail


class DeliveryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryDetail
        fields = '__all__'