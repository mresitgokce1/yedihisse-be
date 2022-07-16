from django.db import models
from yedihisse.models import BaseEntity
from django.utils.translation import gettext as _
from address.models import Address
from phone.models import PhoneNumber
from user.models import CustomUser
from animal.models import AnimalType


class Slaughterhouse(BaseEntity):
    slaughterhouse_name = models.CharField(verbose_name=_("Kesimhane Adı"), max_length=50, blank=False)
    description = models.CharField(verbose_name=_("Açıklama"), max_length=250, blank=False)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, verbose_name=_("Kesimhane Adresi"), null=True,
                                   related_name="r_address_of_slaughterhouse",
                                   related_query_name="q_address_of_slaughterhouse")
    phone = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE, verbose_name=_("Kesimhane Telefonu"), null=True,
                              related_name="r_phone_of_slaughterhouse",
                              related_query_name="q_phone_of_slaughterhouse")

    def __str__(self):
        return self.slaughterhouse_name


class SlaughterhouseJoinType(BaseEntity):
    holding_capacity = models.PositiveSmallIntegerField(verbose_name=_("Hayvan Tutma Kapasitesi"), default=0,
                                                        null=False, blank=False)
    killing_capacity = models.PositiveSmallIntegerField(verbose_name=_("Aynı Anda Kesim Kapasitesi"), default=0,
                                                        null=False, blank=False)
    shredding_capacity = models.PositiveSmallIntegerField(verbose_name=_("Aynı Anda Parçalama Kapasitesi"), default=0,
                                                          null=False, blank=False)
    slaughterhouse_type = models.ForeignKey(AnimalType, on_delete=models.SET_NULL, null=True,
                                            verbose_name=_("Kesimhane Tipi"),
                                            related_name="r_type_of_slaughterhouse",
                                            related_query_name="q_type_of_slaughterhouse")
    slaughterhouse = models.ForeignKey(Slaughterhouse, on_delete=models.CASCADE, verbose_name=_("Kesimhane"),
                                       related_name="r_slaughterhouse_of_type",
                                       related_query_name="q_slaughterhouse_of_type")

    def __str__(self):
        return str(self.holding_capacity)


class SlaughterhouseManagerMission(BaseEntity):
    slaughterhouse_manager_mission_type_name = models.CharField(verbose_name=_("Kesimhane Görevlisi Görev Tip Adı"),
                                                                max_length=50, blank=False)
    description = models.CharField(verbose_name=_("Açıklama"), max_length=250, blank=True)

    def __str__(self):
        return self.slaughterhouse_manager_mission_type_name


class SlaughterhouseManager(BaseEntity):
    description = models.CharField(verbose_name=_("Açıklama"), max_length=100, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_("Kesimhaneye Atanan Görevli"),
                             related_name="r_manager_of_slaughterhouse",
                             related_query_name="q_manager_of_slaughterhouse")
    slaughterhouse = models.ForeignKey(Slaughterhouse, on_delete=models.CASCADE,
                                       verbose_name=_("Görevliye Atanan Kesimhane"),
                                       related_name="r_slaughterhouse_of_manager",
                                       related_query_name="q_slaughterhouse_of_manager")
    slaughterhouse_manager_mission = models.ForeignKey(SlaughterhouseManagerMission, on_delete=models.SET_NULL,
                                                       null=True,
                                                       related_name="r_mission_of_manager",
                                                       related_query_name="q_mission_of_manager")

    def __str__(self):
        return self.description
