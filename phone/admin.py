from django.contrib import admin
from phone.models import PhoneNumber, PhoneNumberType

admin.site.register(PhoneNumber)
admin.site.register(PhoneNumberType)
