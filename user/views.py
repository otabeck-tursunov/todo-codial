from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView

from .models import *
from .serializers import *


class RegisterAPIView(APIView):
    @swagger_auto_schema(
        request_body=UserPostSerializer
    )
    def post(self, request):
        serializer = UserPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Muvaffaqiyatli ro'yxatdan o'tildi!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteAPIView(APIView):
    def delete(self, request):
        if request.user.is_authenticated:
            request.user.delete()
            return Response("User muvaffaqiyatli o'chirildi!", status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserDetailsAPIView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserUpdateAPIView(APIView):
    @swagger_auto_schema(
        request_body=UserUpdateSerializer
    )
    def put(self, request):
        if request.user.is_authenticated:
            user = request.user
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("User ma'lumoti muvaffaqiyatli o'zgartirildi!", status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class ChangePasswordAPIView(APIView):
    @swagger_auto_schema(
        request_body=ChangePasswordSerializer
    )
    def patch(self, request):
        if request.user.is_authenticated:
            user = request.user
            serializer = ChangePasswordSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Password muvaffaqiyatli o'zgartirild!", status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
