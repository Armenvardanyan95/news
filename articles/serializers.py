from rest_framework import serializers
from .models import Article
from stats.models import Share
from magazines.models import Magazine
from topics.serializers import TopicSerializer
from utils.general import string_likeness, generate_index


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    url = serializers.HyperlinkedIdentityField(view_name='article-detail')
    magazine = serializers.HyperlinkedRelatedField(view_name='magazine-detail', queryset=Magazine.objects.all(),
                                                   lookup_field='slug')
    magazine_details = serializers.JSONField(source='get_magazine_details', read_only=True)

    topics = TopicSerializer(read_only=True, many=True)
    is_shared = serializers.SerializerMethodField()
    is_saved = serializers.SerializerMethodField()

    class Meta:
        model = Article
        exclude = ('randomizer', 'index',)
        extra_kwargs = {
            'topics': {'write_only': True}
        }

    def create(self, validated_data):

        title = validated_data['title']
        others = Article.objects.values('title', 'index')

        for article in others:
            if string_likeness(title, article['title']) > 75:
                validated_data['index'] = article['index']
                return super().create(validated_data)
        validated_data['index'] = generate_index(Article)
        return super().create(validated_data)

    def get_is_shared(self, instance):

        request = self.context['request']
        if not request.user.is_authenticated():
            return False

        return instance.share_set.filter(user=request.user).exists()

    def get_is_saved(self, instance):

        request = self.context['request']
        if not request.user.is_authenticated():
            return False

        return instance in request.user.saved_articles.all()
