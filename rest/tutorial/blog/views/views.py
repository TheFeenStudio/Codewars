from django.shortcuts import render
from rest_framework import viewsets, permissions
from blog.models import Blogs
from blog.serializers import BlogSerializator


class Blog(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BlogSerializator
