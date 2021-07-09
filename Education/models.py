from django.db import models
from django.db.models.fields.files import ImageField
from ckeditor.fields import RichTextField
from django.utils.html import format_html
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.utils.timezone import now
from embed_video.fields import EmbedVideoField
  
# Create your models here.

TAGS = (('Technology', 'Technology'), ('Health service', 'Health service'), ('Education', 'Education'), ('Others', 'Others'))
    
class Education(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    video = EmbedVideoField(default='')  # same like models.URLField()
    image = CloudinaryField('image', default="")
   #  image=models.ImageField(upload_to= "images", default="blog.jpg", null=True, blank=True)
    author=models.CharField(max_length=14)
    tags=models.CharField(choices=TAGS, max_length=100, default='Technology')
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    content=RichTextField()
    # is_deleted=models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return self.title + " by " + self.author


class Careers(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    skill=models.CharField(max_length=500)
    experience=models.CharField(max_length=255)
    timeStamp=models.DateTimeField(blank=True)
    content=RichTextField()
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)

class Recruitment(models.Model):
    sno=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    email= models.CharField(max_length=100)
    phone= models.CharField(max_length=100)
    code= models.CharField(max_length=10)
    lcompany= models.CharField(max_length=255)
    city= models.CharField(max_length=255)
    state= models.CharField(max_length=255)
    experience=models.CharField(max_length=255)
    upload_file=models.FileField(upload_to='')
    content=RichTextField()
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)






