from rest_framework import routers
from blog.views.views import BlogView
from django.urls import path, include


urlpatterns = {
    path('blog/', BlogView.as_view())
}