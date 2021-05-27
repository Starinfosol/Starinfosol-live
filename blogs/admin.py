from django.contrib import admin
from django.db.models.fields.files import ImageField
from django.utils.html import format_html
from blogs.models import Post, BlogComment


class PostAdmin(admin.ModelAdmin):
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





class BlogCommentAdmin(admin.ModelAdmin):
        list_display = ('sno', 'comment', 'user', 'post', 'parent')
        search_fields = ['comment', 'user', 'post']
        list_per_page = 10
        list_filter = ['created_at']
        list_display_links = ['comment', 'user', 'post']


admin.site.register(Post, PostAdmin)
# admin.site.register(BlogComment)
admin.site.register(BlogComment, BlogCommentAdmin)




