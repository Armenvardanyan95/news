from rest_framework import serializers
from .models import Topic
from utils.transliteration import transliterate


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    url = serializers.HyperlinkedIdentityField(view_name='topic-detail')

    class Meta:
        model = Topic
        exclude = ('randomizer', 'keywords',)

    def create(self, validated_data):
        validated_data['keywords'] = transliterate(validated_data['title'])
        return super().create(validated_data)
