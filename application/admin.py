from django.contrib import admin
from application.models import Application, ApplicationStatusType, ApplicationStatus


admin.site.register(Application)
admin.site.register(ApplicationStatusType)
admin.site.register(ApplicationStatus)
