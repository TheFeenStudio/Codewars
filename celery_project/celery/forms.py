from django import forms
from .models import MailBox


class ContactForm(forms.ModelForm):
    class Meta:
        model = MailBox
        fields = '__all__'