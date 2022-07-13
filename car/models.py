from django.db import models
from yedihisse.models import BaseEntity
from user.models import CustomUser
from phone.models import PhoneNumber
from django.utils.translation import gettext as _


class CarMissionType(BaseEntity):
    car_mission_type_name = models.CharField(verbose_name=_("Araç Görev Tip Adı"), max_length=50, blank=False)
    description = models.CharField(verbose_name=_("Açıklama"), max_length=250, blank=True)

    def __str__(self):
        return self.car_mission_type_name


class CarType(BaseEntity):
    car_type_name = models.CharField(verbose_name=_("Araç Tip Adı"), max_length=50, blank=False)
    description = models.CharField(verbose_name=_("Araç Tip Açıklaması"), max_length=250, blank=True)

    def __str__(self):
        return self.car_type_name


class Car(BaseEntity):
    car_name = models.CharField(verbose_name=_("Araba Adı"), max_length=50, blank=False)
    car_number_plate = models.CharField(verbose_name=_("Araç Plakası"), max_length=20, blank=True)
    cattle_capacity = models.PositiveSmallIntegerField(verbose_name=_("Büyükbaş Kapasitesi"),
                                                       null=True, blank=True)
    ovine_capacity = models.PositiveSmallIntegerField(verbose_name=_("Küçükbaş Kapasitesi"),
                                                      null=True, blank=True)
    is_awning = models.BooleanField(verbose_name=_("Araç Tenteli Mi?"), blank=True, null=True, default=False)
    car_type = models.ForeignKey(CarType, on_delete=models.SET_NULL, verbose_name=_("Araç Tipi"), null=True,
                                 related_name="r_type_of_car", related_query_name="q_type_of_car")
    phone_number = models.ForeignKey(PhoneNumber, on_delete=models.SET_NULL, verbose_name=_("Aracın numarası"),
                                     null=True, related_name="r_phone_of_car", related_query_name="q_phone_of_car")
    car_mission_type = models.ForeignKey(CarMissionType, on_delete=models.SET_NULL, verbose_name=_("Araç Görev Tipi"),
                                         null=True,
                                         related_name="r_mission_of_car", related_query_name="q_mission_of_car")

    def __str__(self):
        return self.car_name


class CarManagerMission(BaseEntity):
    car_manager_mission_type_name = models.CharField(verbose_name=_("Araç Görevlisinin Görev Tip Adı"), max_length=50,
                                                     blank=False)
    description = models.CharField(verbose_name=_("Açıklama"), max_length=250, blank=True)

    def __str__(self):
        return self.car_manager_mission_type_name


class CarManager(BaseEntity):
    description = models.CharField(verbose_name=_("Açıklama"), max_length=250, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_("Araca Atanacak Görevli"),
                                related_name="r_manager_of_car", related_query_name="q_manager_of_car")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name=_("Görevlinin Atanacağı Araç"),
                               related_name="r_car_of_manager", related_query_name="q_car_of_manager")
    car_manager_mission = models.ForeignKey(CarManagerMission, on_delete=models.SET_NULL,
                                            verbose_name=_("Araç Görevlisinin Görevi"),
                                            null=True, related_name="r_mission_of_manager",
                                            related_query_name="q_mission_of_manager")

    def __str__(self):
        return f'{self.car} - {self.user}'
