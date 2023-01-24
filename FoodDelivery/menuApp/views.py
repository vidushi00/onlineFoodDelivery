from django.shortcuts import render

from menuApp.models import Menu

from menuApp.serializers import MenuSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def index():
    return "Welcome to menu listing app"


@api_view(['GET'])
def get_all_menu_by_restaurant_id(request, restaurant_id):
    try:
        menu_object = Menu.objects.filter(restaurant_id=restaurant_id)
        serialized_data = MenuSerializer(menu_object, many=True)
        return Response({'status': 'Success', 'response': serialized_data.data})
    except Exception as e:
        return Response({'status': 'Fail', 'response': str(e)})


@api_view(['GET'])
def get_menu_by_id(request, id):
    try:
        menu_object = Menu.objects.filter(id=id)
        serialized_data = MenuSerializer(menu_object, many=True)
        return Response({'status': 'Success', 'response': serialized_data.data})
    except Exception as e:
        return Response({'status': 'Fail', 'response': str(e)})


@api_view(['POST'])
def post_menu_details(request):
    try:
        data = request.data
        serialized_data = MenuSerializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'status': 'Success', 'message': 'Dish created successfully'})
        return Response({'status': 'Fail', 'message': serialized_data.errors})
    except Exception as e:
        return Response({'status': 'Fail', 'response': str(e)})