from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'item', 'transaction_date', 'amount', 'is_successful','amount','is_successful','stripe_payment_intent_id','stripe_charge_id']
