from django.contrib import admin
from killing.models import KillingGroup, KillingGroupType, KillingJoinAnimal, KillingStatusType

admin.site.register(KillingGroup)
admin.site.register(KillingGroupType)
admin.site.register(KillingJoinAnimal)
admin.site.register(KillingStatusType)
