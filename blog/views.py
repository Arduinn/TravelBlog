from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, "blog/index.html", {})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactForm() 
        return render(request, 'blog/contact.html', {'form':form}) 

    
