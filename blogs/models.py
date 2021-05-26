from django.db import models
from django.db.models.fields.files import ImageField
from ckeditor.fields import RichTextField
from django.utils.html import format_html
from django.db import models
from cloudinary.models import CloudinaryField
  

# Create your models here.

TAGS = (('Technology', 'Technology'), ('Health service', 'Health service'), ('Education', 'Education'), ('Others', 'Others'))
    
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    image = CloudinaryField('image', default="")
    # image=models.ImageField(upload_to= "images", default="blog.jpg", null=True, blank=True)
    author=models.CharField(max_length=14)
    tags=models.CharField(choices=TAGS, max_length=100, default='Technology')
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    content=RichTextField()
    # is_deleted=models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)


    # def photo_tag(self):
    #     return u'<img src="%s" />' % self.image.url
    def photo_tag(self, obj):
        return u'<img src="/media/{obj.image}" />' % self.image.url
    photo_tag.short_description = 'image'
    photo_tag.allow_tags = True


    def __str__(self):
        return self.title + " by " + self.author

    