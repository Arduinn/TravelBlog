from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
import datetime
from .models import Contact, Post

# Create your views here.
def home(request):
    return render(request, "blog/index.html", {})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()
    return render(request, 'blog/contact.html', {}) 

def contact_ans(request):
    contact_list = Contact.objects.last() 
    return render(request, 'blog/contact_ans.html', {'contact_list': contact_list})

def posts_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/posts_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
