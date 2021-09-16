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
