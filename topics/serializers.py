from rest_framework import serializers
from .models import Topic
from utils.transliteration import transliterate


class TopicSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Topic

    def get_is_subscribed(self, instance):
        request = self.context['request']
        if not request.user.is_authenticated():
            return False
        return instance in request.user.topics.all()


class TopicRetrieveSerializer(TopicSerializer):
    id = serializers.ReadOnlyField()
    url = serializers.HyperlinkedIdentityField(view_name='topic-detail')

    class Meta:
        model = Topic
        exclude = ('randomizer', 'keywords',)

    def create(self, validated_data):
        validated_data['keywords'] = transliterate(validated_data['title'])
        return super().create(validated_data)

    def get_is_subscribed(self, instance):
        request = self.context['request']
        if not request.user.is_authenticated():
            return False

        return instance in request.user.topics.all()


class TopicListSerializer(TopicSerializer):

    class Meta:
        model = Topic
        exclude = ('randomizer', 'keywords', 'abbr_eng', 'abbr_arm', 'related_topics', 'title_eng',)

