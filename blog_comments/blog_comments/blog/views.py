from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Blog
from blog.serializer import BlogSerializator
from django.http import HttpResponse


class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializator


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializator


def Index(request):
    return HttpResponse('<a href="/blog">Blog</a>')