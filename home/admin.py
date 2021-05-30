from django.contrib import admin
from .models import Contact
from django.db.models.fields.files import ImageField
from django.utils.html import format_html
from .models import Edu


class EduAdmin(admin.ModelAdmin):
        # readonly_fields=['photo_tag']
        list_display = ('title', 'author', 'tags', 'less_content')
        list_filter = ('tags', 'created_at')
        radio_fields = {"tags" : admin.HORIZONTAL}
        list_per_page = 4
        search_fields = ['title', 'content', 'author', 'tags']
        # prepopulated_fields = {'slug': ('title',)}
        # summernote_fields = ('content',)
        list_display_links = ['title', 'less_content']

        def less_content(self, obj):
                return obj.content[:50]
                # return format_html(f'<span style="color:green">{obj.content[:100]}</span>')

        # def photo_tag(self, obj):
        #         return format_html(f'<img src="{{post.image.url}}" style="height:100px;width:100px>')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'content', 'is_deleted')
    # list_filter = ('is_deleted', 'created_at', ('phone', admin.EmptyFieldListFilter))
    list_filter = ('created_at', 'is_deleted')
    list_per_page = 20
    search_fields = ['name', 'phone', 'email', 'content']
    list_display_links = ['name', 'email', 'phone', 'content']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Edu, EduAdmin)