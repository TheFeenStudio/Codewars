from django.contrib import admin
from django.urls import path, include
from blog.views import BlogView, BlogDetail
from blog.views import Index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', BlogView.as_view(), name="contact"),
    path('blog/<int:pk>/', BlogDetail.as_view()),
    path('', Index),
]
