from django.contrib import admin
from application.models import Application, ApplicationStatusType, ApplicationStatus


admin.site.register(Application)
admin.site.register(ApplicationStatusType)
admin.site.register(ApplicationStatus)

admin.site.site_header = "Seni Seviyorum Şuram <3"
admin.site.site_title = "Seni Seviyorum Şuram <3"
admin.site.index_title = "Seni Seviyorum Şuram <3"