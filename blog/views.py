from django.shortcuts import render, get_list_or_404, get_object_or_404,redirect
from django.core.mail import send_mail
from django.http import HttpResponseForbidden, Http404, HttpResponseRedirect, HttpResponse
from django.db import models
from django.utils import timezone
import datetime
from .models import Contact, Post, Photo
from .forms import ContactForm

# Create your views here.
def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "blog/index.html", {'posts': posts})

def about(request):
    return render(request, "blog/about.html", {})

def contact(request): 
    if request.method == 'POST':
        form  = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact_ans/')
    else:
        form = ContactForm() 
    return render(request, 'blog/contact.html', {'form': form}) 

def contact_ans(request):
    return render(request, 'blog/contact_ans.html', {}) 

def posts_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/posts_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def photo_list(request):
    photos = Photo.objects.filter(timestamp__lte=timezone.now()).order_by('timestamp')
    return render(request, 'blog/gallery.html', {'photos': photos}) 
