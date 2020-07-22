from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'naslov_knjige', 'ime_pisca', 'prezime_pisca', 'jezik', 'is_published', 'list_date')
    list_display_links = ('id', 'naslov_knjige')
    list_filter = ('prezime_pisca',)
    list_editable = ('is_published',)
    search_fields = ('naslov_knjige', 'prezime_pisca', 'ime_pisca')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)