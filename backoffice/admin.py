from django.contrib import admin
from backoffice.models import Author, Publisher, Title
from django.utils.html import format_html

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Title)
