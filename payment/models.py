from django.db import models
from yedihisse.models import BaseEntity
from django.utils.translation import gettext as _
from address.models import Address
from phone.models import PhoneNumber
from company.models import Company
from user.models import CustomUser


class Payment(BaseEntity):
    pass


class PaymentOption(BaseEntity):
    pass


class PaymentType(BaseEntity):
    pass

