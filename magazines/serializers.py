from rest_framework import serializers
from .models import Magazine


class MagazineSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    url = serializers.HyperlinkedIdentityField(view_name='magazine-detail', lookup_field='slug')
    randomizer = serializers.ReadOnlyField()

    class Meta:
        model = Magazine
        exclude = ('admin', )
