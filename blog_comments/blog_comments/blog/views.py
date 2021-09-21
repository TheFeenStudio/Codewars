from rest_framework.views import APIView
from rest_framework.response import Response
from models import Blog
from serializer import BlogSerializator


class BlogView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializator(blogs, many=True)
        return Response({'blog': serializer.data})