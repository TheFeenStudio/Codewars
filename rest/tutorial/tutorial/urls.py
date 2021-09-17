from django.contrib import admin
from django.urls import path, include
from blog.views.views import BlogView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('blog.urls')),
    path('', BlogView.as_view(), name="contact")
]

