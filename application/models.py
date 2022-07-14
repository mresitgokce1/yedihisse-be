from django.db import models
from yedihisse.models import BaseEntity
from django.utils.translation import gettext as _
from allotment.models import Allotment
from user.models import CustomUser
from animal.models import AnimalType
from branch.models import Branch


class Application(BaseEntity):
    description = models.CharField(verbose_name=_("Başvuru Açıklama"), max_length=250, blank=True)
    allotment_rate = models.PositiveSmallIntegerField(verbose_name=_("Hisse Oranı(1-7)"), blank=False, null=False,
                                                      default=1)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, verbose_name=_("Başvuran Kullanıcı"),
                             related_name="r_user_of_application", related_query_name="q_user_of_application")
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, verbose_name=_("Başvuru Yapılan Şube"),
                               related_name="r_branch_of_application", related_query_name="q_branch_of_application")
    allotment = models.ForeignKey(Allotment, on_delete=models.SET_NULL, null=True, verbose_name=_("Başvurulan Hisse"),
                                  related_name="r_allotment_of_application",
                                  related_query_name="q_allotment_of_application")
    animal_type = models.ForeignKey(AnimalType, on_delete=models.SET_NULL, null=True,
                                    verbose_name=_("Başvuran Kullanıcı"),
                                    related_name="r_animal_type_of_application",
                                    related_query_name="q_animal_type_of_application")

    def __str__(self):
        return self.description


class ApplicationStatusType(BaseEntity):
    application_status_type_name = models.CharField(verbose_name=_("Başvuru Statü Tip Adı"), max_length=100,
                                                    blank=False)

    def __str__(self):
        return self.application_status_type_name


class ApplicationStatus(BaseEntity):
    application = models.ForeignKey(Application, on_delete=models.SET_NULL, null=True, verbose_name=_("Başvuru"),
                                    related_name="r_status_of_application",
                                    related_query_name="q_status_of_application")
    application_status_type = models.ForeignKey(ApplicationStatusType, on_delete=models.SET_NULL, null=True,
                                                verbose_name=_("Başvuru Statü"),
                                                related_name="r_type_of_application",
                                                related_query_name="q_type_of_application")

    def __str__(self):
        return ".."
