from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from backoffice.models import Author, Publisher, Title
from .models import Reservation

admin.site.register(Author)
admin.site.register(Publisher)

class TitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover_image')
    search_fields = ['title', 'authors__name']  # Assuming authors have a 'name' field

    def cover_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height:auto;">', obj.image.url)
        return "Aucune image"
    cover_image.short_description = "Aperçu de l'image"

admin.site.register(Title, TitleAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'reservation_date', 'end_date', 'is_active', 'duration')
    list_filter = ('is_active', 'reservation_date', 'end_date')
    search_fields = ('user__username', 'title__title')
    actions = ['archive_reservations']

    def duration(self, obj):
        if obj.end_date:
            return (obj.end_date - obj.reservation_date).days
        elif obj.is_active:
            return (timezone.now() - obj.reservation_date).days
        return "N/A"
    duration.short_description = "Durée (jours)"

    def archive_reservations(self, request, queryset):
        queryset.update(is_active=False, end_date=timezone.now())
    archive_reservations.short_description = "Archiver les réservations sélectionnées"

admin.site.register(Reservation, ReservationAdmin)
