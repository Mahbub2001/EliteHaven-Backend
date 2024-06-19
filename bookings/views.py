from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from hostadvertisements.models import Advertisement
from datetime import datetime
from rest_framework.authentication import TokenAuthentication
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data.copy()
        data['user'] = user.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        item = serializer.validated_data['item']
        number_of_persons = serializer.validated_data['number_of_persons']
        from_date = serializer.validated_data['from_date']
        to_date = serializer.validated_data['to_date']
        subtotal=serializer.validated_data['subtotal']
        if not item.availability:
            return Response({"detail": "This item is currently unavailable."}, status=status.HTTP_400_BAD_REQUEST)

        if Booking.objects.filter(item=item, is_completed=False).exists():
            return Response({"detail": "This item is currently booked by another user."}, status=status.HTTP_400_BAD_REQUEST)

        data['subtotal'] = subtotal
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
