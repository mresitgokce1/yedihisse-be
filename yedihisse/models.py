from django.db import models
from user.models import CustomUser
from django.utils.translation import gettext as _


class BaseEntity(models.Model):
    id = models.AutoField(primary_key=True, verbose_name=_("Id"))
    joined_by_user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL,
                                           verbose_name=_("Oluşturan Kullanıcı"),
                                           blank=False, null=True,
                                           related_name="%(app_label)ss_%(class)s_related",
                                           related_query_name="%(app_label)ss_%(class)ss")
    date_joined = models.DateTimeField(verbose_name=_("Oluşturulma Tarihi"),
                                        auto_now_add=True,
                                        blank=False, null=False)
    modified_by_user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL,
                                            verbose_name=_("Değiştiren Kullanıcı"),
                                            blank=False, null=True,
                                            related_name="%(app_label)s_%(class)s_related",
                                            related_query_name="%(app_label)s_%(class)ss")
    date_modified = models.DateTimeField(verbose_name=_("Değiştirilme Tarihi"),
                                         auto_now=True,
                                         blank=False, null=False)
    is_active = models.BooleanField(verbose_name=_("Aktif Mi?"), default=True,
                                    blank=False, null=False)
    is_deleted = models.BooleanField(verbose_name=_("Silindi Mi?"), default=False,
                                     blank=False, null=False)

    class Meta:
        abstract = True
