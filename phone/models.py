from django.db import models
from django.utils.translation import gettext as _
from yedihisse.models import BaseEntity


class PhoneNumberType(BaseEntity):
    number_type_name = models.CharField(verbose_name=_("Telefon Tip Adı"), blank=False, max_length=50)

    def __str__(self):
        return self.number_type_name


class PhoneNumber(BaseEntity):
    description = models.CharField(verbose_name=_("Telefon Açıklaması"), blank=True, max_length=250)
    number = models.CharField(verbose_name=_("Telefon Numarası"), blank=False, max_length=25)
    number_type = models.ForeignKey(PhoneNumberType, on_delete=models.SET_NULL, verbose_name=_("Telefon Tipi"),
                                    blank=False, null=True,
                                    related_name="r_type_of_phone", related_query_name="q_type_of_phone")

    def __str__(self):
        return self.number

