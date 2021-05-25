from django.contrib import admin
from django.db.models.fields.files import ImageField
from blogs.models import Post
from django.utils.html import format_html
# Register your models here.


class PostAdmin(admin.ModelAdmin):
        readonly_fields=['photo_tag']
        list_display = ('title', 'author', 'photo_tag', 'tags', 'less_content')
        list_filter = ('tags', 'created_at')
        radio_fields = {"tags" : admin.HORIZONTAL}
        list_per_page = 4
        search_fields = ['title', 'content', 'author', 'tags']
        # prepopulated_fields = {'slug': ('title',)}
        # summernote_fields = ('content',)
        list_display_links = ['title', 'less_content']

        def less_content(self, obj):
                # return obj.content[:50]
                return format_html(f'<span style="color:green">{obj.content[:100]}</span>')

        def photo_tag(self, obj):
                return format_html(f'<img src="/media/{obj.image}" style="height:100px;width:100px>')



admin.site.register(Post, PostAdmin)