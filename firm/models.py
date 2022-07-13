from django.db import models
from yedihisse.models import BaseEntity
from django.utils.translation import gettext as _
from address.models import Address
from phone.models import PhoneNumber
from company.models import Company
from user.models import CustomUser


class Firm(BaseEntity):
    firm_name = models.CharField(verbose_name=_("Firma Adı"), blank=False, max_length=50)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, verbose_name=_("Firmanın Şirketi"),
                                related_name="r_firm_of_company", related_query_name="q_firm_of_company")
    address = models.OneToOneField(Address, on_delete=models.CASCADE, verbose_name=_("Firma Adresi"), null=True)
    phone = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE, verbose_name=_("Firma Telefonu"), null=True)

    def __str__(self):
        return self.firm_name


class FirmManagerMission(BaseEntity):
    firm_manager_mission_type_name = models.CharField(verbose_name=_("Firma Görevlisi Görev Tip Adı"), max_length=50,
                                                      blank=False)
    description = models.CharField(verbose_name=_("Açıklama"), max_length=250, blank=True)

    def __str__(self):
        return self.firm_manager_mission_type_name


class FirmManager(BaseEntity):
    description = models.CharField(verbose_name=_("Açıklama"), max_length=100, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_("Firmaya Atanacak Görevli"),
                             related_name="r_manager_of_firm", related_query_name="q_manager_of_firm")
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name=_("Görevliye Atanan Firma"),
                             related_name="r_firm_of_manager", related_query_name="q_firm_of_manager")
    firm_manager_mission = models.ForeignKey(FirmManagerMission, on_delete=models.SET_NULL, null=True,
                                             related_name="r_mission_of_manager",
                                             related_query_name="q_mission_of_manager")

    def __str__(self):
        return self.description
