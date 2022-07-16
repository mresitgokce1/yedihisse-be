from django.db import models
from django.utils.translation import gettext as _
from yedihisse.models import BaseEntity


class AddressType(BaseEntity):
    address_type_name = models.CharField(verbose_name=_("Adres Tip Adı"), blank=False, max_length=50, unique=True)

    def __str__(self):
        return self.address_type_name


class Country(BaseEntity):
    country = models.CharField(verbose_name=_("Ülke"), blank=False, max_length=200, unique=True)

    def __str__(self):
        return self.country


class City(BaseEntity):
    city = models.CharField(verbose_name=_("Şehir"), blank=False, max_length=200)
    linked_country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name=_("Bağlı Ülke"),
                                       related_name="r_country_of_city", related_query_name="q_country_of_city")

    def __str__(self):
        return self.city


class District(BaseEntity):
    district = models.CharField(verbose_name=_("İlçe"), blank=False, max_length=200)
    linked_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name=_("Bağlı Şehir"),
                                    related_name="r_city_of_district", related_query_name="q_city_of_district")

    def __str__(self):
        return self.district


class Parish(BaseEntity):
    parish = models.CharField(verbose_name=_("Mahalle"), blank=False, max_length=200)
    linked_district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name=_("Bağlı İlçe"),
                                        related_name="r_parish_of_district", related_query_name="q_parish_of_district")

    def __str__(self):
        return self.parish


class Address(BaseEntity):
    address_name = models.CharField(verbose_name=_("Adres Adı"), blank=True, max_length=50)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, verbose_name=_("Ülke"), blank=False, null=True,
                                related_name="r_country_address", related_query_name="q_country_address")
    city = models.ForeignKey(City, on_delete=models.SET_NULL, verbose_name=_("Şehir"), blank=False, null=True,
                             related_name="r_city_of_address", related_query_name="q_city_of_address")
    district = models.ForeignKey(District, on_delete=models.SET_NULL, verbose_name=_("İlçe"), blank=False, null=True,
                                 related_name="r_district_of_address", related_query_name="q_district_of_address")
    parish = models.ForeignKey(Parish, on_delete=models.SET_NULL, verbose_name=_("Mahalle"), blank=False, null=True,
                               related_name="r_parish_of_address", related_query_name="q_parish_of_address")
    street = models.CharField(verbose_name=_("Sokak"), blank=True, max_length=200)
    apartment_name = models.CharField(verbose_name=_("Apartman Adı"), blank=True, max_length=200)
    apartment_no = models.CharField(verbose_name=_("Apartman No"), blank=True, max_length=200)
    apartment_block_name = models.CharField(verbose_name=_("Apartman Blok Adı/No"), blank=True, max_length=200)
    floor_no = models.CharField(verbose_name=_("Kat No"), blank=True, max_length=200)
    flat_no = models.CharField(verbose_name=_("Daire No"), blank=True, max_length=200)
    address_detail = models.CharField(verbose_name=_("Açık Adres"), blank=True, max_length=300)
    address_direction = models.CharField(verbose_name=_("Adres Tarifi"), blank=True, max_length=300)
    address_type = models.ForeignKey(AddressType, on_delete=models.SET_NULL, verbose_name=_("Adres Tipi"),
                                     blank=False, null=True,
                                     related_name="r_type_of_address", related_query_name="q_type_of_address")

    def __str__(self):
        return self.address_name

