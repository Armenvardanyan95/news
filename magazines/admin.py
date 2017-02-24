from django.contrib import admin
from .models import Magazine


class MagazineAdmin(admin.ModelAdmin):
    fields = [field.name for field in Magazine._meta.fields if field.name != "id"]

    class Meta:
        model = Magazine

admin.site.register(Magazine, MagazineAdmin)
