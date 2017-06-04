from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'brief', 'reference', 'image', 'magazine',  'topics', )
    filter_horizontal = ('topics',)
    list_display = ('magazine', 'title',)
    show_full_result_count = True
    save_as = True

    class Meta:
        model = Article

admin.site.register(Article, ArticleAdmin)
