from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from AccountApp.serializers import UserRegistrationSerializer, UserLoginSerializer

from django.http.response import JsonResponse

# Create your views here.

class RegisterUserView(GenericAPIView):

    def post(self, request):
        register_serializer = UserRegistrationSerializer(data=request.data)
        if register_serializer.is_valid(raise_exception=True):
            register_serializer.save()
            return JsonResponse(register_serializer.data, safe=False, status=201)
        return JsonResponse(register_serializer.errors, safe=False, status=400)

class LoginUserView(GenericAPIView):

    def post(self, request):
        login_serializer = UserLoginSerializer(data=request.data, context={'request': request})
        login_serializer.is_valid(raise_exception=True)
        return JsonResponse(login_serializer.data, status=200)