from django.contrib import admin
from .models import Contact
from django.db.models.fields.files import ImageField
from django.utils.html import format_html


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'content', 'is_deleted')
    # list_filter = ('is_deleted', 'created_at', ('phone', admin.EmptyFieldListFilter))
    list_filter = ('created_at', 'is_deleted')
    list_per_page = 20
    search_fields = ['name', 'phone', 'email', 'content']
    list_display_links = ['name', 'email', 'phone', 'content']


admin.site.register(Contact, ContactAdmin)
