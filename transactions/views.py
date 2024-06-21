from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
from hostadvertisements.models import Advertisement
from bookings.models import Booking

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data.copy()
        data['user'] = user.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        item = serializer.validated_data['item']
        if not Booking.objects.filter(user=user, item=item, is_completed=False).exists():
            return Response({"detail": "You can only perform transactions on items you have booked."}, status=status.HTTP_400_BAD_REQUEST)

        if Transaction.objects.filter(item=item, is_successful=True).exists():
            return Response({"detail": "This item has already been successfully booked and paid for by another user."}, status=status.HTTP_400_BAD_REQUEST)

        transaction = serializer.save()

        if transaction.is_successful:
            item.availability = False
            item.save()
            Booking.objects.filter(item=item, is_completed=False).update(is_completed=True)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)