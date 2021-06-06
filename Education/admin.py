from django.contrib import admin
from django.db.models.fields.files import ImageField
from django.utils.html import format_html
from .models import Education, Careers, Recruitment
from embed_video.admin import AdminVideoMixin

class EducationAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


class EducationAdmin(admin.ModelAdmin):
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

class CareersAdmin(admin.ModelAdmin):
        list_display = ('sno', 'title', 'skill', 'experience', 'timeStamp', 'less_content')
        list_filter = ['created_at']
        list_per_page = 4
        search_fields = ['title', 'content', 'experience', 'skill']
        list_display_links = ['title', 'less_content']

        def less_content(self, obj):
                return obj.content[:50]
                # return format_html(f'<span style="color:green">{obj.content[:100]}</span>')

class RecruitmentAdmin(admin.ModelAdmin):
        list_display = ('sno', 'fname', 'email', 'phone', 'experience', 'state', 'code', 'less_content')
        list_filter = ['created_at', 'code']
        list_per_page = 4
        search_fields = ['fname', 'email', 'phone', 'experience', 'state', 'code']
        list_display_links = ['fname', 'email', 'phone', 'code']

        def less_content(self, obj):
                return obj.content[:50]
                # return format_html(f'<span style="color:green">{obj.content[:100]}</span>')


admin.site.register(Education, EducationAdmin)
admin.site.register(Careers, CareersAdmin)
admin.site.register(Recruitment, RecruitmentAdmin)
