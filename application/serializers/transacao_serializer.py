from rest_framework import serializers
from application.serializers.validators.transacao_validator import invalid_value

class TransacaoResponseSerializer(serializers.Serializer):

    account_number = serializers.CharField(read_only=True)
    account_holder = serializers.CharField(read_only=True)
    balance = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)


class TransacaoRequestSerializer(serializers.Serializer):

    value = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate(self, attrs):

        if invalid_value(attrs['value']):
            raise ValueError('O valor da transação tem que ser um numero positivo')
        
        return attrs
    
class TransferenciaRequestSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    value = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate(self, attrs):

        if invalid_value(attrs['value']):
            raise ValueError('O valor da transação tem que ser um numero positivo')
        
        return attrs