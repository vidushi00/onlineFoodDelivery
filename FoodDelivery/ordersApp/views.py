from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
# Create your views here.

import stripe
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

import cartApp
from ordersApp.serializers import OrderSerializer

from menuApp.models import Menu

from ordersApp.models import Orders

# This is your test secret API key.
stripe.api_key = settings.STRIPE_SECRET_KEY
endpoint_secret =settings.STRIPE_WEBHOOK_SECRET


def index():
    return "This is orders view"


@api_view(['GET'])
def get_all_orders_by_user(request, user_id):
    order_object = Orders.objects.filter(user_id=user_id)
    serialized_data = OrderSerializer(order_object, many=True)
    if serialized_data:
        return Response({'status': 'Success', 'response': serialized_data.data})
    return Response({'status': 'Fail', 'response': serialized_data.errors})


@csrf_exempt
@api_view(['POST'])
def create_checkout_session(request):
    host = request.get_host()
    data = request.data
    price = []
    order_id = ""
    quantity = []
    print(request.data)
    for each in data:
        dish_detail = Menu.objects.filter(id=each['food_id']).first()
        order_id = "".join(str(each["id"]))
        quantity.append(each["quantity"])
        price.append(int(dish_detail.price))

    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                'price_data': {
                    'currency': 'inr',
                    'unit_amount': sum(price),
                    'product_data': {
                        'name': order_id
                    }
                },
                'quantity': sum(quantity),
            },
        ],
        mode='payment',
        success_url= 'http://{}{}'.format(host, reverse('payment-success')),
        cancel_url= 'http://{}{}'.format(host, reverse('payment-fail'))
    )
    return redirect(checkout_session.url, code=303)


def save_order(request):
    try:
        for each in request:
            order_data = Orders(food_id=each['food_id'], user_id=each['user_id'], restaurant_id=each['restaurant_id'], quantity=each['quantity'])
            serialized_data = OrderSerializer(data=order_data, many=True)
            if serialized_data.is_valid():
                serialized_data.save()
            cartApp.remove_item_from_cart(each["id"])
        return Response({'status': 'Success', 'response': "Order saved!"})
    except Exception as e:
        return Response({'status': 'Fail', 'response': str(e)})


def payment_success(request):
    save_order(request.data)
    return "Payment Successfully Done!"


def payment_fail(request):
    return "Payment Failed!"


@csrf_exempt
def webhook_view(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    print(sig_header)
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Passed signature verification

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        if session.payment_status == 'paid':
            pass

    return HttpResponse(status=200)

