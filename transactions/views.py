import stripe
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.conf import settings
from .models import Transaction
from .serializers import TransactionSerializer
from bookings.models import Booking

stripe.api_key = settings.STRIPE_SECRET_KEY  

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

        try:
            intent = stripe.PaymentIntent.create(
                amount=int(serializer.validated_data['amount'] * 100),  # Convert amount to cents
                currency='usd',
                metadata={'integration_check': 'accept_a_payment'},
            )
            data['stripe_payment_intent_id'] = intent['id']
        except stripe.error.StripeError as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        transaction = serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = request.data.copy()

        if 'is_successful' in data and data['is_successful']:
            intent_id = instance.stripe_payment_intent_id
            try:
                intent = stripe.PaymentIntent.confirm(intent_id)
                data['stripe_charge_id'] = intent['charges']['data'][0]['id']
            except stripe.error.StripeError as e:
                return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
