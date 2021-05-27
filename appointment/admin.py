from django.contrib import admin
from .models import Appointment
from django.utils.html import format_html
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'department', 'doctor', 'information', 'is_deleted')
    list_filter = ('doctor', 'is_deleted', 'created_at')
    list_per_page = 15
    search_fields = ['doctor', 'name', 'email', 'phone', 'date']
    list_display_links = ['name', 'email', 'phone', 'information']
    # list_filter = ('is_deleted', 'created_at', ('doctor', admin.EmptyFieldListFilter))



    # def email(self, obj):
    #     return format_html(f'<span style="color:green">{obj.content[:100]}</span>')



admin.site.register(Appointment, AppointmentAdmin)



 