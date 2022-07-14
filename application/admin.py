from django.contrib import admin
from application.models import Application, ApplicationStatusType, ApplicationStatus


admin.site.register(Application)
admin.site.register(ApplicationStatusType)
admin.site.register(ApplicationStatus)

admin.site.site_header = "UMSRA Admin"
admin.site.site_title = "UMSRA Admin Portal"
admin.site.index_title = "Welcome to UMSRA Researcher Portal"