from django.db import models
from django.db.models.fields.files import ImageField
from ckeditor.fields import RichTextField
from django.utils.html import format_html
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.utils.timezone import now
  
# Create your models here.

TAGS = (('Technology', 'Technology'), ('Health service', 'Health service'), ('Education', 'Education'), ('Others', 'Others'))
    
class Edu(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
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
# Create your models here.


class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=100)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp= models.DateTimeField(auto_now_add=True, blank=True)
     is_deleted=models.BooleanField(default=False)
     created_at = models.DateField(auto_now_add=True, blank=True, null=True)

     def __str__(self):
        return self.name



