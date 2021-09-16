from rest_framework import serializers
<<<<<<< HEAD
from .models import Blogs
=======
from blog.models import Blogs
>>>>>>> 1c3b26634dd2b724a818c058c742b101cfba0bef




class BlogSerializator(serializers.ModelSerializer):
    class Meta:
        model = Blogs
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = '__all__'


>>>>>>> 1c3b26634dd2b724a818c058c742b101cfba0bef
