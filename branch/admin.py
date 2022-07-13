from django.contrib import admin
from branch.models import Branch, BranchManagerMission, BranchManager


admin.site.register(Branch)
admin.site.register(BranchManagerMission)
admin.site.register(BranchManager)