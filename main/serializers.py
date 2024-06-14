from rest_framework import serializers

from user.serializers import UserSerializer
from .models import *


class RejaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reja
        fields = '__all__'


class RejaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reja
        fields = ('id', 'sarlavha', 'batafsil', 'muddat')


class RejaTahrirlashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reja
        fields = ('sarlavha', 'batafsil', 'muddat', 'bajarildi')
