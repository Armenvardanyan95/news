from django.contrib import admin
from .models import Topic


class TopicAdmin(admin.ModelAdmin):
    fields = ('title', 'related_topics', 'abbr_arm', 'abbr_eng', 'title_eng')
    readonly_fields = ('randomizer', 'keywords',)
    filter_horizontal = ('related_topics',)

    class Meta:
        model = Topic

admin.site.register(Topic, TopicAdmin)
