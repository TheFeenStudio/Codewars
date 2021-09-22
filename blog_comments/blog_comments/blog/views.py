from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Blog, Comment
from blog.serializer import BlogSerializator, CommentSerializer
from django.http import HttpResponse


class BlogView(APIView):
    def get(self, request):
        queryset = Blog.objects.all()
        serializer = BlogSerializator(queryset, many=True)
        return Response({'blog': serializer.data})



class BlogDetail(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializator


def Index(request):
    return HttpResponse('<a href="/blog">Blog</a>')