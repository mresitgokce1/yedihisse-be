from django.db import models
from yedihisse.models import BaseEntity
from django.utils.translation import gettext as _
from slaughterhouse.models import Slaughterhouse
from animal.models import Animal


class KillingGroupType(BaseEntity):
    killing_group_type_name = models.CharField(verbose_name=_("Kesim Grubu Tip Adı"), blank=False, max_length=50)

    def __str__(self):
        return self.killing_group_type_name


class KillingGroup(BaseEntity):
    killing_group_name = models.CharField(verbose_name=_("Kesim Grup Adı"), blank=False, max_length=50)
    description = models.CharField(verbose_name=_("Açıklama"), blank=True, max_length=250)
    slaughterhouse = models.ForeignKey(Slaughterhouse, on_delete=models.SET_NULL, null=True,
                                       verbose_name=_("Kesim Grubunun Kesimhanesi"),
                                       related_name="r_slaughterhouse_of_killing_group",
                                       related_query_name="q_slaughterhouse_of_killing_group")
    killing_group_type = models.ForeignKey(KillingGroupType, on_delete=models.SET_NULL, null=True,
                                           verbose_name=_("Kesim Grubu Tipi"),
                                           related_name="r_type_of_killing_group",
                                           related_query_name="q_type_of_killing_group")

    def __str__(self):
        return self.killing_group_name


class KillingStatusType(BaseEntity):
    killing_status_type_name = models.CharField(verbose_name=_("Kesim Durumu Tip Adı"), max_length=50, blank=False)
    description = models.CharField(verbose_name=_("Açıklama"), max_length=250, blank=True)


class KillingJoinAnimal(BaseEntity):
    killing_number = models.PositiveSmallIntegerField(verbose_name=_("Kesim Sıra Numarası"), blank=False, null=False)
    killing_status = models.ForeignKey(KillingStatusType, on_delete=models.SET_NULL, null=True,
                                       verbose_name=_("Kesim Durumu"),
                                       related_name="r_status_of_killing", related_query_name="q_status_of_killing")

    killing_group = models.ForeignKey(KillingGroup, on_delete=models.CASCADE, verbose_name=_("Kesim Grubu"),
                                      related_name="r_killing_group_of_animal",
                                      related_query_name="q_killing_group_of_animal")
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name=_("Kesime Alınan Hayvan"),
                               related_name="r_animal_of_killing_group", related_query_name="q_animal_of_killing_group")

    def __str__(self):
        return self.killing_number



