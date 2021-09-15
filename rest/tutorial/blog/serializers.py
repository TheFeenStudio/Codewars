from rest_framework import serializers
from .models import Blogs
from rest_framework.views import APIView

# class BlogSerializator(serializers.Serializer):
#     title = serializers.CharField()
#     description = serializers.CharField()
#     image = serializers.ImageField()
#     date = serializers.DateField()

class BlogSerializator(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'
