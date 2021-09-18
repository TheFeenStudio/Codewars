from django.views.generic import CreateView
from .forms import ContactForm
from .models import MailBox
from .service import send


class ContactView(CreateView):
    model = MailBox
    forms_class = ContactForm
    success_url = '/'
    template_name = 'index.html'
    fields = '__all__'

    def form_valid(self, form):
        form.save()
        send(form.instance.email)
        return super().form_valid(form)