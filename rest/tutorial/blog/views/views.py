<<<<<<< HEAD
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
=======
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Blogs
from blog.serializers import BlogSerializator


class BlogView(APIView):
    def get(self, request):
        blogs = Blogs.objects.all()
        serializer = BlogSerializator(blogs, many=True)
        return Response({'blog': serializer.data})
>>>>>>> 1c3b26634dd2b724a818c058c742b101cfba0bef
