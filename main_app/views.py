from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import post, Like , Label
from django.conf import settings
from django.contrib.auth.models import User
from core.settings import MEDIA_ROOT, MEDIA_URL
# Create your views here.

def home(request):
    new_posts = post.objects.order_by('-created_at')[:3]
    prg_label = Label.objects.get(title_label = "programming")
    dm_label = Label.objects.get(title_label = "digital marketing")
    pg_last_posts = post.objects.filter(label = prg_label).order_by('-created_at')[:3]
    dm_last_posts = post.objects.filter(label = dm_label).order_by('-created_at')[:3]
    return render( request , 'home.html' , {'last_posts':new_posts,
                                            'prg_posts':pg_last_posts,
                                            'dm_posts':dm_last_posts
                                            })


def blog(request):
    posts = post.objects.all().order_by('-created_at')
    return render(request , 'blog.html' , {'data':posts,
                                            })


def label(request , label_text):
    label_data =Label.objects.get(title_label = label_text)
    posts_data = post.objects.filter(label = label_data).order_by('-created_at')
    return render(request,'label.html',{'data':posts_data , 'label_name':label_data})

def posts(request , posts_pk):
    post_data = post.objects.get(id = posts_pk)
    return render(request , 'posts.html' , {'data' : post_data})


def author(request, name):
    author = User.objects.get(username=name)
    post_data = post.objects.filter(author=author).order_by('-created_at')
    return render(request,'author.html',{'data':post_data ,'author_name':author  })
    