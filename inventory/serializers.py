from rest_framework import serializers
from .models import Item, Allocation, DistributionHistory


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allocation
        fields = '__all__'


class DistributionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DistributionHistory
        fields = '__all__'
