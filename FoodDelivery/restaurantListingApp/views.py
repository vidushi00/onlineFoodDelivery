from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from restaurantListingApp.models import Restaurants
from restaurantListingApp.serializers import RestaurantSerializer


# Create your views here.
def index():
    return Response("Welcome to restaurant listing app!")

@api_view(['GET'])
def get_all_restaurants(request):
    try:
        restaurant_object = Restaurants.objects.all()
        serialized_list = RestaurantSerializer(restaurant_object, many=True)
        return Response({'status': 'Success', 'response': serialized_list.data})
    except Exception as e:
        return Response({'status': 'Fail', 'response': str(e)})


@api_view(["GET"])
def get_restaurant_by_id(request, id):
    try:
        restaurant_object = Restaurants.objects.filter(id=id).first()
        serialized_list = RestaurantSerializer(restaurant_object)
        return Response({'status': 'Success', 'response': serialized_list.data})
    except Exception as e:
        return Response({'status': 'Fail', 'response': str(e)})


@api_view(['POST'])
def post_restaurant_details(request):
    try:
        restaurant_data = request.data
        serialized_data = RestaurantSerializer(data=restaurant_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'status': 'Success', 'message': 'Restaurant created successfully'})
    except Exception as e:
        return Response({'status': 'Fail', 'response': str(e)})


