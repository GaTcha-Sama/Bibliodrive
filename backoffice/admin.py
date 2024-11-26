from django.contrib import admin
from backoffice.models import Author, Publisher, Title
from django.utils.html import format_html

admin.site.register(Author)
admin.site.register(Publisher)

class TitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover_image')

    def cover_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height:auto;">', obj.image.url)
        return "Aucune image"
    cover_image.short_description = "Aperçu de l'image"

admin.site.register(Title, TitleAdmin)