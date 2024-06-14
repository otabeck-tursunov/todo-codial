from django.urls import path
from .views import *

urlpatterns = [
    path('rejalar/', RejalarAPIView.as_view()),
    path('rejalar/<int:reja_id>/', RejaAPIView.as_view()),
    path('reja-qo\'shish/', RejaPostAPIView.as_view()),
    path('rejalar/<int:reja_id>/tahrirlash/', RejaTahrirlashAPIView.as_view()),
    path('rejalar/<int:reja_id>/o\'chirish/', RejaDeleteAPIView.as_view()),
]