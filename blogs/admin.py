from django.contrib import admin
from django.db.models.fields.files import ImageField
from blogs.models import Post
from django.utils.html import format_html
# Register your models here.


class PostAdmin(admin.ModelAdmin):
        readonly_fields=['photo_tag']
        list_display = ('title', 'author', 'photo_tag', 'tags', 'slug', 'content', 'is_deleted')
        list_filter = ('is_deleted', 'created_at', ('author', admin.EmptyFieldListFilter))
        radio_fields = {"tags" : admin.HORIZONTAL}
        list_per_page = 2



        def photo_tag(self, obj):
                return format_html(f'<img src="/media/{obj.image}" style="height:100px;width:100px>')

        # def content(self, obj):
        #         return format_html(f'<span style="color:green">{obj.content[:100]}</span>')


admin.site.register(Post, PostAdmin)