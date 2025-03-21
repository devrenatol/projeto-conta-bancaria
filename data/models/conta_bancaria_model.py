from django.db import models
from django.utils import timezone

class ContaBancariaModel(models.Model):
    
    account_number = models.CharField(max_length=100, blank=False, null=False, unique=True)
    account_holder = models.CharField(max_length=100, blank=False, null=False)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'data'