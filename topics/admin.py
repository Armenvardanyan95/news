from django.contrib import admin
from .models import Topic


class TopicAdmin(admin.ModelAdmin):
    fields = ('title', 'related_topics', 'keywords')
    readonly_fields = ('randomizer',)

    class Meta:
        model = Topic

admin.site.register(Topic, TopicAdmin)
