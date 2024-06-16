from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from transactions.models import Transaction
from hostadvertisements.models import Advertisement

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data.copy()
        data['user'] = user.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        item = serializer.validated_data['item']
        transaction = serializer.validated_data['transaction']

        if not Transaction.objects.filter(user=user, item=item, is_successful=True).exists():
            return Response({"detail": "You can only review items after completing a successful transaction."}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        review = serializer.save()
        review.item.save() 

