from django.contrib import admin
from address.models import Address, AddressType, Country, City, District, Parish

admin.site.register(Address)
admin.site.register(AddressType)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Parish)