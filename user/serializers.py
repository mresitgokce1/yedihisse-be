from user.models import CustomUser
from django.contrib.auth.models import Group
from rest_framework import serializers


#HyperlinkedModelSerializer -> groups bağlantısı için primar key değeri yerine, normal değeri gösterir. Admin(1), NormalUser(2)'i düşünürsek.
#HyperlinkedModelSerializer -> gropus altında Admin, NormalUser yazar.
#ModelSerializer -> gropus altında 1,2 yazar.
class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url', 'phone', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']