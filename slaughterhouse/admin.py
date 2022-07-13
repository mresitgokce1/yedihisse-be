from django.contrib import admin
from slaughterhouse.models import Slaughterhouse, SlaughterhouseJoinType, SlaughterhouseManager, \
    SlaughterhouseManagerMission

admin.site.register(Slaughterhouse)
admin.site.register(SlaughterhouseJoinType)
admin.site.register(SlaughterhouseManager)
admin.site.register(SlaughterhouseManagerMission)
