from decimal import Decimal

def invalid_value(value):
    return Decimal(value) < 0