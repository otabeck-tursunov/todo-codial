from django.shortcuts import render, get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class RejaAPIView(APIView):
    def get(self, request, reja_id):
        if request.user.is_authenticated:
            reja = get_object_or_404(Reja, id=reja_id)
            serializer = RejaSerializer(reja)
            return Response(serializer.data, status=200)


class RejalarAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='bajarildi',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_BOOLEAN,
            ),
            openapi.Parameter(
                name='vaqt',
                description="Yaratilgan vaqti bo'yicha tartiblash!",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                enum=['yangi', 'eski']
            )
        ]
    )
    def get(self, request):
        if request.user.is_authenticated:
            rejalar = Reja.objects.filter(user=request.user)

            filter_bajarildi = request.query_params.get('bajarildi', None)
            filter_vaqt = request.query_params.get('vaqt', None)

            if filter_bajarildi == 'true':
                rejalar = rejalar.filter(bajarildi=True)
            elif filter_bajarildi == 'false':
                rejalar = rejalar.filter(bajarildi=False)

            if filter_vaqt == 'yangi':
                rejalar = rejalar.order_by('-created_at')
            elif filter_vaqt == 'eski':
                rejalar = rejalar.order_by('created_at')

            serializer = RejaSerializer(rejalar, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class RejaPostAPIView(APIView):
    @swagger_auto_schema(
        request_body=RejaPostSerializer,
    )
    def post(self, request):
        if request.user.is_authenticated:
            serializer = RejaPostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response("Reja muvaffaqiyatli qo'shildi!", status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=401)


class RejaTahrirlashAPIView(APIView):
    @swagger_auto_schema(
        request_body=RejaTahrirlashSerializer,
    )
    def put(self, request, reja_id):
        if request.user.is_authenticated:
            reja = get_object_or_404(Reja, id=reja_id)
            serializer = RejaTahrirlashSerializer(reja, request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response("Reja muvaffaqiyatli o'zgartirildi!", status=status.HTTP_200_OK)
            return Response(serializer.errors, status=400)
        return Response(status=401)


class RejaDeleteAPIView(APIView):
    @swagger_auto_schema(
        responses={
            204: openapi.Response(description="Reja muvaffaqiyatli o'zgartirildi!"),
            400: openapi.Response(description="User faqat o'ziga tegishli bo'lgan rejalarni o'chira oladi!"),
            401: openapi.Response(description="Foydalanuvchi autentifikatsiya qilinmagan"),
        }
    )
    def delete(self, request, reja_id):
        if request.user.is_authenticated:
            reja = get_object_or_404(Reja, id=reja_id)
            if reja.user == request.user:
                reja.delete()
                return Response("Reja muvaffaqiyatli o'chirildi!", status=204)
            return Response("User faqat o'ziga tegishli bo'lgan rejalarni o'chira oladi!",
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(status=401)


class RejaDestroyAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Reja.objects.all()
    serializer_class = RejaSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
