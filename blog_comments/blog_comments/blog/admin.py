from django.contrib import admin
from blog.models import Blog
from blog.models import Users
from blog.models import Comment
from blog.models import Reply_comment


admin.site.register(Blog)
admin.site.register(Users)
admin.site.register(Comment)
admin.site.register(Reply_comment)