from django import forms
from .models import MailBox


class ContactForm(forms.ModelForm):
    class Meta:
        app_label = 'app'
        model = MailBox
        fields = '__all__'
