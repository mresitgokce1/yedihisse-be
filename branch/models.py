from django.db import models
from yedihisse.models import BaseEntity
from django.utils.translation import gettext as _
from address.models import Address
from phone.models import PhoneNumber
from user.models import CustomUser


class BranchManagerMission(BaseEntity):
    branch_manager_mission_type_name = models.CharField(verbose_name=_("Şube Görevlisi Görev Tip Adı"), max_length=50,
                                                        blank=False)
    description = models.CharField(verbose_name=_("Açıklama"), max_length=250, blank=True)

    def __str__(self):
        return self.branch_manager_mission_type_name


class Branch(BaseEntity):
    branch_name = models.CharField(verbose_name=_("Şube Adı"), max_length=50, blank=False)

    #firm todo firm model.
    address = models.OneToOneField(Address, on_delete=models.CASCADE, verbose_name=_("Şube Adresi"), null=True)
    phone = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE, verbose_name=_("Şube Telefonu"), null=True)

    def __str__(self):
        return self.branch_name


class BranchManager(BaseEntity):
    description = models.CharField(verbose_name=_("Açıklama"), max_length=100, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_("Şubeye Atanacak Görevli"),
                             related_name="r_manager_of_branch", related_query_name="q_manager_of_branch")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name=_("Görevliye Atanan Şube"),
                               related_name="r_branch_of_manager", related_query_name="q_branch_of_manager")
    branch_manager_mission = models.ForeignKey(BranchManagerMission, on_delete=models.SET_NULL, null=True,
                                               related_name="r_mission_of_manager",
                                               related_query_name="q_mission_of_manager")