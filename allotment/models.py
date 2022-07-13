from django.db import models
from yedihisse.models import BaseEntity
from django.utils.translation import gettext as _
from animal.models import Animal


class Allotment(BaseEntity):
    description = models.CharField(verbose_name=_("Hisse Açıklama"), max_length=250, blank=True)
    allotment_prepay_price = models.DecimalField(verbose_name=_("Hisse Ön Ödeme Fiyatı"), blank=False, null=False,
                                                 default=0)
    allotment_price = models.DecimalField(verbose_name=_("Hisse Fiyatı"), blank=False, null=False, default=0)
    allotment_killing_price = models.DecimalField(verbose_name=_("Hisse Kesim Fiyatı"), blank=False, null=False,
                                                  default=0)
    animal = models.OneToOneField(Animal, on_delete=models.SET_NULL, null=True, verbose_name=_("Hissenin Hayvanı"),
                                  related_name="r_animal_of_allotment", related_query_name="q_animal_of_allotment")

    def __str__(self):
        return self.description