from django.contrib import admin
from .models import Topic, Article, Magazine

class MagazineAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Magazine._meta.fields][1:]
    save_as = True

admin.site.register(Magazine, MagazineAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Article._meta.fields]
    save_as = True

admin.site.register(Article, ArticleAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Topic._meta.fields]
    save_as = True

admin.site.register(Topic, TopicAdmin)