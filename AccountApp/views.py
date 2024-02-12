from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from AccountApp.serializers import UserRegistrationSerializer, UserLoginSerializer, PasswordResetRequestViewSerializer, SetNewPasswordSerializer, LogoutUserViewSerializer
from .models import User
from django.http.response import JsonResponse
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

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

class PasswordResetRequestView(GenericAPIView):

    def post(self, request):
        reset_serializer = PasswordResetRequestViewSerializer(data=request.data, context={'request': request})
        reset_serializer.is_valid(raise_exception=True)
        return JsonResponse({"message": "A link has been sent to you to reset your password"}, status=200, safe=False)

class PasswordResetConfirm(GenericAPIView):

    def get(self, request, uidb64, token):
        try:
            user_id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return JsonResponse({"message": "Token is invalid or has expired"}, status=401)
            return Response({'success': True, 'message': "Credentials are valid", 'uidb64': uidb64, 'token':token, 'status':200})
        except DjangoUnicodeDecodeError:
            return JsonResponse({"message": "Token is invalid or has expired"}, status=401, safe = False)

class SetNewPassword(GenericAPIView):
    def patch(self, request):
        new_password_serializer = SetNewPasswordSerializer(data=request.data)
        new_password_serializer.is_valid(raise_exception=True)
        return JsonResponse({"message": "Password Reset Successful"}, status=200, safe = False)

@permission_classes([IsAuthenticated])
class LogoutUserView(GenericAPIView):
    def post(self, request):
        logout_serializer = LogoutUserViewSerializer(data=request.data)
        logout_serializer.is_valid(raise_exception=True)
        logout_serializer.save()
        return Response(status=204)


