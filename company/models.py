from django.db import models
from yedihisse.models import BaseEntity
from django.utils.translation import gettext as _
from address.models import Address
from phone.models import PhoneNumber
from user.models import CustomUser


class Company(BaseEntity):
    company_name = models.CharField(verbose_name=_("Şirket Adı"), blank=False, max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, verbose_name=_("Şirket Adresi"), null=True)
    phone = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE, verbose_name=_("Şirket Telefonu"), null=True)

    def __str__(self):
        return self.company_name


class CompanyManagerMission(BaseEntity):
    company_manager_mission_type_name = models.CharField(verbose_name=_("Şirket Görevlisi Görev Tip Adı"),
                                                         max_length=50, blank=False)
    description = models.CharField(verbose_name=_("Açıklama"), max_length=250, blank=True)

    def __str__(self):
        return self.company_manager_mission_type_name


class CompanyManager(BaseEntity):
    description = models.CharField(verbose_name=_("Açıklama"), max_length=100, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_("Şirkete Atanacak Görevli"),
                             related_name="r_manager_of_company", related_query_name="q_manager_of_company")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_("Görevliye Atanan Şirket"),
                                related_name="r_company_of_manager", related_query_name="q_company_of_manager")
    company_manager_mission = models.ForeignKey(CompanyManagerMission, on_delete=models.SET_NULL, null=True,
                                                related_name="r_mission_of_manager",
                                                related_query_name="q_mission_of_manager")

    def __str__(self):
        return self.description
