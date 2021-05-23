from django.db import models
from django.db.models.fields.files import ImageField
from ckeditor.fields import RichTextField

# Create your models here.

TAGS = (('Technology', 'Technology'), ('Health service', 'Health service'), ('Education', 'Education'), ('Others', 'Others'))
    
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to= "images", default="")
    # image = models.ImageField(upload_to ='uploads/% Y/% m/% d/')
    # image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,)
    author=models.CharField(max_length=14)
    tags=models.CharField(choices=TAGS, max_length=100, default='Technology')
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    content=RichTextField()
    is_deleted=models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title + " by " + self.author

    