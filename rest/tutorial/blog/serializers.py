from rest_framework import serializers
from blog.models import Blogs

# class BlogSerializator(serializers.Serializer):
#     title = serializers.CharField()
#     description = serializers.CharField()
#     image = serializers.ImageField()
#     date = serializers.DateField()



class BlogSerializator(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'


