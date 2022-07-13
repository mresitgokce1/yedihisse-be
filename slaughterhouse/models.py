from django.db import models
from yedihisse.models import BaseEntity
from django.utils.translation import gettext as _
from address.models import Address
from phone.models import PhoneNumber
from company.models import Company
from user.models import CustomUser


class SlaughterhouseJoinType(BaseEntity):
    pass


class SlaughterhouseManager(BaseEntity):
    pass


class Slaughterhouse(BaseEntity):
    pass


class SlaughterhouseType(BaseEntity):
    pass


