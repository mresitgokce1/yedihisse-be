from django.contrib import admin
from slaughterhouse.models import Slaughterhouse, SlaughterhouseType, SlaughterhouseJoinType, SlaughterhouseManager

admin.site.register(Slaughterhouse)
admin.site.register(SlaughterhouseType)
admin.site.register(SlaughterhouseJoinType)
admin.site.register(SlaughterhouseManager)
