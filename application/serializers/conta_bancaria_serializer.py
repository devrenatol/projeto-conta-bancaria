from rest_framework import serializers
from application.serializers.validators.conta_bancaria_validator import invalid_account_holder, invalid_account_number, invalid_balance

class ContaBancariaResponseSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    account_number = serializers.CharField(read_only=True)
    account_holder = serializers.CharField(read_only=True)
    balance = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

class ContaBancariaRequestSerializer(serializers.Serializer):

    account_number = serializers.CharField(max_length=8, required=True)
    account_holder = serializers.CharField(max_length=100, required=True)
    balance = serializers.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def validate(self, attrs):
        if invalid_account_number(attrs['account_number']):
            raise serializers.ValidationError({'account_number': 'O numero da conta esta no formato errado. Formato: 99999-99'})
        
        if invalid_account_holder(attrs['account_holder']):
            raise serializers.ValidationError({'account_holder': 'O nome do cliente da conta so pode conter letras'})
        
        if invalid_balance(attrs['balance']):
            raise serializers.ValidationError({'balance': 'O saldo da conta tem que ser um número positivo'})
        
        return attrs