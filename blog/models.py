# import os
from django.conf import settings

from django.db import models
# from django.contrib.auth.models import User
from django.forms import ImageField
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField

from django.urls import reverse


STATUS = (          #tuple
    (0,"Draft"),
    (1,"Publish")
)

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name='blog_posts')   # https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#referencing-the-user-model ; https://stackoverflow.com/questions/24629705/django-using-get-user-model-vs-settings-auth-user-model
    updated_on = models.DateTimeField(auto_now=True)
    intro = RichTextField(blank=True, null=True)      #new 11-16-22
    recipe = RichTextField(blank=True, null=True)      #new 11-16-22
    meta_description = models.CharField(max_length=150, blank=False) #new 5-2-23
    # intro = models.TextField()      #new 11-16-22
    # recipe = models.TextField()     #new 11-16-22
    # story = models.TextField()      #new 11-16-22
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='images', null=True, blank=False)
    image_alt = models.CharField(max_length=150, blank=True) #new 5-3-23

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # return reverse('post_detail', args=[str(self.id)])
        return reverse('post_detail', args=[str(self.slug)])

class PostImage(models.Model):  
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    image_alt = models.CharField(max_length=150, blank=True) #new 5-3-23

    def __str__(self):
        return self.post.title