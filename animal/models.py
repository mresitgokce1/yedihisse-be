from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _
from yedihisse.models import BaseEntity
from car.models import Car


class AnimalType(BaseEntity):
    animal_type_name = models.CharField(verbose_name=_("Hayvan Tip Adı"), blank=False, max_length=50, unique=True)
    can_allotment = models.BooleanField(verbose_name=_("Hayvan Hisse Edilebilir Mi?"), null=False, default=False)

    def __str__(self):
        return self.animal_type_name


class Animal(BaseEntity):
    age = models.FloatField(verbose_name="Hayvan Yaşı", default=0, blank=False, null=False,
                            validators=[MinValueValidator(0), MaxValueValidator(50)])
    kilo = models.FloatField(verbose_name=_("Hayvan Kilosu"), default=0, blank=False, null=False,
                             validators=[MinValueValidator(0), MaxValueValidator(1000)])
    code = models.CharField(verbose_name=_("Hayvan Kodu"), blank=False, max_length=255, unique=True)
    cost = models.FloatField(verbose_name=_("Hayvan Maliyeti"), default=0, blank=False, null=False)
    gain = models.FloatField(verbose_name=_("Hayvan Karı"), default=0, blank=False, null=False)
    ear_code = models.CharField(verbose_name=_("Hayvan Kulak Kodu"), blank=True, max_length=255)
    bait_code = models.CharField(verbose_name=_("Hayvan Yem Kodu"), blank=True, max_length=255)
    animal_type = models.ForeignKey(AnimalType, on_delete=models.SET_NULL, verbose_name=_("Hayvanın Tipi"),
                                    blank=False, null=True,
                                    related_name="r_type_of_animal", related_query_name="q_type_of_animal")
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, verbose_name=_("Hayvanın Aracı"), null=True,
                            related_name="r_car_of_animal", related_query_name="q_car_of_animal")

    def __str__(self):
        return self.code

