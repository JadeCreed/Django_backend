from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Item, Allocation, DistributionHistory
from .serializers import (
    ItemSerializer,
    AllocationSerializer,
    DistributionHistorySerializer,
)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class AllocationViewSet(viewsets.ModelViewSet):
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer

    @action(detail=True, methods=['post'])
    def distribute(self, request, pk=None):
        allocation = self.get_object()

        if allocation.distributed:
            return Response(
                {"error": "Already distributed"},
                status=status.HTTP_400_BAD_REQUEST
            )

        item = allocation.item
        quantity = allocation.allocated_quantity

        if item.total_stock < quantity:
            return Response(
                {"error": "Not enough stock"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Deduct stock
        item.total_stock -= quantity
        item.save()

        # Mark allocation as distributed
        allocation.distributed = True
        allocation.save()

        # Create history record
        DistributionHistory.objects.create(
            item=item,
            barangay=allocation.barangay,
            quantity=quantity,
        )

        return Response({"status": "Distribution successful"})
