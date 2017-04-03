from rest_framework import serializers
from .models import Magazine


class MagazineSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    url = serializers.HyperlinkedIdentityField(view_name='magazine-detail', lookup_field='slug')
    randomizer = serializers.ReadOnlyField()
    is_subscribed = serializers.SerializerMethodField()
    some_topics = serializers.ListField(source="get_some_topics")

    def get_is_subscribed(self, instance):
        request = self.context['request']
        if not request.user.is_authenticated(): 
            return False

        return instance in request.user.magazines.all()

    class Meta:
        model = Magazine
        exclude = ('admin', )
