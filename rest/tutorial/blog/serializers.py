from rest_framework import serializers
from blog.models import Blogs


class BlogSerializator(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'