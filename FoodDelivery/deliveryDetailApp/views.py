from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from deliveryDetailApp.models import DeliveryDetail
from deliveryDetailApp.serializers import DeliveryDetailSerializer


# Create your views here.
def index():
    return "This is delivery detail service"


@api_view(['GET'])
def get_delivery_detail_by_user_id(request, user_id):
    try:
        delivery_detail = DeliveryDetail.objects.filter(user_id=user_id)
        serialized_data = DeliveryDetailSerializer(delivery_detail).data
        return Response({'status': 'Success', 'response': serialized_data})
    except Exception as e:
        return Response({'status': 'Fail', 'response': str(e)})


@api_view(['POST'])
def save_delivery_detail(request):
    try:
        delivery_data = request.data
        serialized_data = DeliveryDetailSerializer(data=delivery_data, many=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'status': 'Success', 'response': 'Data saved successfully'})
    except Exception as e:
        return Response({'status': 'Fail', 'response': str(e)})