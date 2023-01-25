import json

from django.shortcuts import render

from cartApp.models import UsersCart
from cartApp.serializers import UsersCartSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from menuApp.models import Menu
from menuApp.serializers import MenuSerializer


# Create your views here.

def index():
    return "Welcome to your cart"


@api_view(['GET'])
def get_all_items_by_user_id(request, user_id):
    try:
        cart_object = UsersCart.objects.filter(user_id=user_id).all()
        serialized_data = UsersCartSerializer(cart_object, many=True).data
        for items in serialized_data:
            menu_item = Menu.objects.filter(id=items["food_id"]).first()
            serialized_menu = MenuSerializer(menu_item).data
            print(serialized_menu)
            items["amount"] = serialized_menu["price"] * items["quantity"]
            print(items["amount"])
        return Response({'status': 'Success', 'response': serialized_data})
    except Exception as e:
        return Response({'status': 'Fail', 'response': str(e)})


@api_view(['POST'])
def add_item_to_cart(request):
    try:
        item_data = request.data
        cart_object = UsersCart.objects.filter(user_id=item_data["user_id"], food_id=item_data["food_id"]).first()
        if cart_object:
            cart_object.quantity += item_data["quantity"]
            cart_object.save()
            return Response({'status': 'Success', 'response': 'Cart item saved successfully'})
        else:
            serialized_data = UsersCartSerializer(data=item_data)
            serialized_data["status"] = "in_cart"
            print(serialized_data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response({'status': 'Success', 'response': 'Cart item saved successfully'})
    except Exception as e:
        return Response({'status': 'Fail', 'response': str(e)})


@api_view(['DELETE'])
def remove_item_from_cart(request, id):
    try:
        item = UsersCart.objects.filter(id=id).first()
        if item:
            item.delete()
            return Response({'status': 'Success', 'response': 'Deleted successfully'})
        return Response({'status': 'Success', 'response': 'Item not present in cart'})
    except Exception as e:
        return Response({'status': 'Fail', 'response': str(e)})


def update_order_status_in_cart(request, id):
    try:
        cart_item = UsersCart.objects.filter(id=id).first()
        serialized_data = UsersCartSerializer(cart_item, request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'status': 'Success', 'response': 'Data updated successfully'})
    except Exception as e:
        return Response({'status': 'Success', 'response': str(e)})

def add_item_to_orders(request):
    pass


