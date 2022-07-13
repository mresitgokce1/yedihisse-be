from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    SEX_CHOICE = (
        ('F', _('KADIN')),
        ('M', _('ERKEK'))
    )

    id = models.AutoField(primary_key=True, verbose_name=_("Id"))
    username = None
    first_name = models.CharField(verbose_name=_('Adı'), max_length=100, blank=True)
    last_name = models.CharField(verbose_name=_('Soyadı'), max_length=50, blank=True)
    sex = models.CharField(verbose_name=_('Cinsiyet'), blank=True, max_length=1, choices=SEX_CHOICE)
    email = models.CharField(verbose_name=_('E-posta'), null=True, blank=True, max_length=100, unique=True)
    primary_phone = models.CharField(verbose_name=_('Telefon Numarası'), blank=False, max_length=25, unique=True)
    phone = models.ForeignKey(to="phone.PhoneNumber", on_delete=models.SET_NULL, verbose_name=_("Kullanıcının Telefonu"),
                              null=True, related_name="r_phone_of_user", related_query_name="q_phone_of_user")
    address = models.ForeignKey(to="address.Address", on_delete=models.SET_NULL, verbose_name=_("Kullanıcının Adresi"),
                                null=True, related_name="r_address_of_user", related_query_name="q_address_of_user")
    is_deleted = models.BooleanField(verbose_name=_("Silindi Mi?"), default=False, blank=False, null=False)
    joined_by_user = models.ForeignKey("self", on_delete=models.SET_NULL,
                                        verbose_name=_("Oluşturan Kullanıcı"),
                                        blank=False, null=True,
                                        related_name="%(app_label)ss_%(class)s_related",
                                        related_query_name="%(app_label)ss_%(class)ss")
    modified_by_user = models.ForeignKey("self", on_delete=models.SET_NULL,
                                         verbose_name=_("Değiştiren Kullanıcı"),
                                         blank=False, null=True,
                                         related_name="%(app_label)s_%(class)s_related",
                                         related_query_name="%(app_label)s_%(class)ss")
    date_modified = models.DateTimeField(verbose_name=_("Değiştirilme Tarihi"),
                                         auto_now=True,
                                         blank=False, null=False)

    USERNAME_FIELD = 'primary_phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.primary_phone

