from rest_framework import serializers
from blog.models import Blog, Users, Comment, Reply_comment


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Users
        fields = '__all__'





class Reply_commentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply_comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    reply = Reply_commentsSerializer(many=True)

    class Meta:
        model = Comment
        fields = '__all__'


class BlogSerializator(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'