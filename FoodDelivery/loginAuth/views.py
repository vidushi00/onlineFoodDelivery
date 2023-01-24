from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from loginAuth.serializers import UserSerializer


# Create your views here.

def index(request):
    return HttpResponse("Welcome to loginAuth view.")

class RegisterViewApi(APIView):
    def post(self, request):
        serialized_data = UserSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'status': 'Success', 'message': 'User created successfully'})
        return Response({'status': 'Fail', 'message': serialized_data.error_messages})

    def get(self, request):
        try:
            user_object = User.objects.all()
            serialized_data = UserSerializer(user_object).data
            return Response({'status': 'Success', 'response': serialized_data})
        except Exception as e:
            return Response({'status': 'Fail', 'response': str(e)})

@api_view(["POST"])
def login_user(request):
    data = {}
    request_data = request.data
    email = request_data['email']
    print(email)
    password = request_data['password']
    try:

        user_object = User.objects.filter(email=email).first()
    except BaseException as e:
        return Response({"Status": 'Fail', 'message': str(e)})

    token = Token.objects.get_or_create(user=user_object)
    print(token)
    if not check_password(password, user_object.password):
        return Response({"status": "Fail", "message": "Incorrect Login credentials"})

    if user_object:
        if user_object.is_active:
            print(request.user)
            login(request, user_object)
            return Response({"Status": "Success", "message": "User Logged In", "token": token[0].key})
        else:
            return Response({"status": "Fail", "message": "Account not active"})
    else:
        raise Response({"status": "Fail", "message": "Account doesnt exist"})