from django.views.generic import CreateView
from ..models.Mail import MailBox
from ..tasks import send_spam_email


class ContactView(CreateView):
    model = MailBox
    success_url = '/'
    template_name = 'index.html'
    fields = '__all__'

    def form_valid(self, form):
        form.save()
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)