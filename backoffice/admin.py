from django.contrib import admin
from backoffice.models import Author, Publisher, Title
from django.utils.html import format_html
from .models import Reservation

admin.site.register(Author)
admin.site.register(Publisher)

class TitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover_image')
    search_fields = ['title', 'authors']

    def cover_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height:auto;">', obj.image.url)
        return "Aucune image"
    cover_image.short_description = "Aperçu de l'image"

admin.site.register(Title, TitleAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'reservation_date', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('user__username', 'title__title')

admin.site.register(Reservation, ReservationAdmin)