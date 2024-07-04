from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
    


class Post(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='users')
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    description = RichTextField(blank=True,null=True)
    tags = models.CharField(max_length=100)
    posted_at = models.DateField(default=datetime.now)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='posts')
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    website = models.CharField(null=True,blank=True,max_length=100)
    commented_at = models.DateTimeField(default=datetime.now)
    comment = models.TextField()
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    