from django.shortcuts import render
from django.core.mail import send_mail
from .models import Contact
# Create your views here.
def home(request):
    return render(request, "blog/index.html", {})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        desc = request.POST.get('desc', '')
        print(name, email, desc)
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()
    return render(request, 'blog/contact.html', {}) 

def contact_ans(request):
    return render(request, 'blog/contact_ans.html', {})

def posts_list(request):
    render(request, 'blog/posts_list.html', {})
