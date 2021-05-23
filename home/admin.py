from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'content', 'is_deleted')
    list_filter = ('is_deleted', 'created_at', ('phone', admin.EmptyFieldListFilter))


admin.site.register(Contact, ContactAdmin)