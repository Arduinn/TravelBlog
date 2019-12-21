from django.forms import ModelForm
from .models import Contact
import datetime

class ContactForm(ModelForm):
    class Meta:
        model = Contact

