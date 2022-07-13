from django.db import models
from yedihisse.models import BaseEntity
from django.utils.translation import gettext as _
from application.models import Application


class PaymentOption(BaseEntity):
    payment_option_name = models.CharField(verbose_name=_("Ödeme Türü Adı"), max_length=100, blank=False)
    description = models.CharField(verbose_name=_("Açıklama"), max_length=250, blank=True)

    def __str__(self):
        return self.payment_option_name


class PaymentType(BaseEntity):
    payment_type_name = models.CharField(verbose_name=_("Ödeme Tipi Adı"), max_length=100, blank=False)
    description = models.CharField(verbose_name=_("Açıklama"), max_length=250, blank=True)

    def __str__(self):
        return self.payment_type_name


class Payment(BaseEntity):
    payment_made = models.DecimalField(verbose_name=_("Yapılan Ödeme"), blank=False, null=False, default=0,
                                          max_digits=15, decimal_places=5)
    receipt_number = models.CharField(verbose_name=_("Ödeme Dekontu"), max_length=100, blank=True)
    description = models.CharField(verbose_name=_("Açıklama"), max_length=250, blank=True)

    application = models.ForeignKey(Application, on_delete=models.SET_NULL, null=True,
                                    verbose_name=_("Ödemenin Yapıldığı Başvuru"),
                                    related_name="r_payment_of_applicaton",
                                    related_query_name="q_payment_of_applicaton")
    payment_type = models.ForeignKey(PaymentType, on_delete=models.SET_NULL, null=True, verbose_name=_("Ödeme Tipi"),
                                     related_name="r_type_of_payment", related_query_name="q_type_of_payment")
    payment_option = models.ForeignKey(PaymentOption, on_delete=models.SET_NULL, null=True,
                                       verbose_name=_("Ödeme Türü"),
                                       related_name="r_option_of_payment", related_query_name="q_option_of_payment")

    def __str__(self):
        return self.receipt_number
