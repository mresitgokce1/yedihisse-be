from django.contrib import admin
from payment.models import Payment, PaymentType, PaymentOption

admin.site.register(Payment)
admin.site.register(PaymentType)
admin.site.register(PaymentOption)

