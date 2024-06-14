from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.validators import EmailValidator
from django_jalali.db import models as jmodels
# Create your models here.
class Label(models.Model):
    title_label = models.CharField(default='title' , max_length=90)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.title_label
    
class post(models.Model):
    title = models.CharField(max_length=500 , blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE )
    label = models.ForeignKey(Label , on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='post_images/' , null=True)
    body = RichTextField()
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    @property
    def like_count(self):
        return self.like_set.count()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'post')
    
class Comment(models.Model):
    post = models.ForeignKey(post, related_name='comments', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255 , blank=False)
    text = models.TextField(blank=True)
    email = models.EmailField(default="emailaddress@gmail.com")
    created_time = jmodels.jDateTimeField(auto_now_add=True)

